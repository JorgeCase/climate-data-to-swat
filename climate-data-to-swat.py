
# Importação de bibliotecas
import os
import pandas as pd
import tkinter as tk
from messages import Messages
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar, Style

# Constantes
HEADER_LINES_TO_READ = 10
MISSING_DATE_FILL_VALUE = -99


# Função para obter o caminho da pasta selecionada pelo usuário
def get_folder_path():
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(title=Messages.SELECT_FOLDER_BUTTON)
    return folder_path


# Função para extrair as informações do cabeçalho do arquivo
def extract_info_from_header(file_path):
    with open(file_path, 'r') as file:
        header_lines = [next(file) for _ in range(10)]

    name_line = header_lines[0]
    code_line = header_lines[1]

    name = name_line.split(': ')[1].strip()
    code = code_line.split(': ')[1].strip()

    return name, code


# Função para remover cabeçalho do arquivo
def remove_header_info(file_path):
    df = pd.read_csv(file_path, sep=';', skiprows=HEADER_LINES_TO_READ)
    return df


# Função para ler arquivos CSV na pasta selecionada
def read_csv_files_in_folder(folder_path):
    csv_files = [
        file for file in os.listdir(folder_path) if file.endswith('.csv')]
    dataframes = {}

    for csv_file in csv_files:
        file_path = os.path.join(folder_path, csv_file)
        try:
            name, code = extract_info_from_header(file_path)
            df = remove_header_info(file_path)
            dataframes[csv_file] = (df, name, code)
        except pd.errors.ParserError:
            print(f"Erro ao ler arquivo '{csv_file}'. Pulando para o próximo.")

    return dataframes


# Função para preencher datas ausentes no DataFrame
def fill_missing_dates(df, date_col):
    df[date_col] = pd.to_datetime(df[date_col])
    date_range = pd.date_range(
        start=df[date_col].min(), end=df[date_col].max(), freq='D')
    df_filled = df.set_index(date_col).reindex(date_range).reset_index()
    df_filled.fillna(MISSING_DATE_FILL_VALUE, inplace=True)
    df_filled = df_filled.rename(columns={'index': 'Data Medicao'})
    return df_filled


# Função para salvar os dados processados em arquivos .txt
def save_to_txt(df_filled, name, code, swat_data_folder):
    for column in df_filled.columns:
        if column != 'Data Medicao' and column != 'Unnamed: 10':
            data_file_name = f"{name}_{code}_{column.replace('/', '_')}.txt"
            data_file_path = os.path.join(swat_data_folder, data_file_name)
            with open(data_file_path, 'w') as data_file:
                data_file.write(
                    df_filled['Data Medicao'].iloc[0].strftime(
                        '%Y%m%d') + "\n")
                df_filled[column].to_csv(
                    data_file, index=False, header=False, sep=' ')


# Classe da aplicação de processamento
class ProcessingApp:
    # Função para construção da interface gráfica
    def __init__(self, root):
        self.root = root
        self.root.title("Climate Data to SWAT")
        self.root.geometry("800x600")
        self.center_window()

        self.folder_path = tk.StringVar()
        self.output_folder = None
        self.saved_files = []

        self.button_style = ("Arial", 12, "bold")
        self.button_text_color = "white"
        self.button_bg_color = "blue"

        self.style = Style()
        self.style.theme_use("clam")
        self.style.configure(
            'custom.Horizontal.TProgressbar',
            troughcolor='white',
            background='blue')

        self.text_style = ("Arial", 12)
        self.text_color = "black"

        self.label = tk.Label(
            self.root,
            text=Messages.INPUT_INSTRUCTIONS,
            font=self.text_style, fg=self.text_color)
        self.label.pack(pady=20)

        self.input_folder_button = tk.Button(
            self.root, text=Messages.SELECT_FOLDER_BUTTON,
            command=self.select_input_folder,
            font=self.button_style,
            fg=self.button_text_color,
            bg=self.button_bg_color)
        self.input_folder_button.pack(pady=10)

        self.file_count_label = tk.Label(
            self.root, text="", font=self.text_style, fg=self.text_color)
        self.file_count_label.pack(pady=10)

        self.execute_button = tk.Button(
            self.root, text=Messages.EXECUTE_BUTTON,
            command=self.execute_processing, state=tk.DISABLED,
            font=self.button_style,
            fg=self.button_text_color,
            bg=self.button_bg_color)
        self.execute_button.pack(pady=10)

        self.progress = Progressbar(
            self.root, orient=tk.HORIZONTAL,
            length=300, mode='determinate',
            style='custom.Horizontal.TProgressbar')
        self.progress.pack(pady=10)

        self.complete_message = tk.Label(
            self.root, text="", font=self.text_style, fg=self.text_color)
        self.complete_message.pack(pady=10)

        self.close_button = tk.Button(
            self.root, text=Messages.CLOSE_BUTTON,
            command=self.root.destroy, state=tk.DISABLED,
            font=self.button_style,
            fg=self.button_text_color,
            bg=self.button_bg_color)
        self.close_button.pack(pady=10)

    # Função para centralizar a aplicação na tela
    def center_window(self):
        # Centralizar a janela na tela
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = 800
        window_height = 500
        x = int((screen_width - window_width) / 2)
        y = int((screen_height - window_height) / 2)
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Função para selecionar a pasta com os dados de entrada
    def select_input_folder(self):
        folder_path = filedialog.askdirectory(
            title=Messages.INPUT_INSTRUCTIONS
        )
        if not folder_path:
            return

        self.folder_path.set(folder_path)
        self.output_folder = os.path.join(folder_path, "output_climate2swat")
        os.makedirs(self.output_folder, exist_ok=True)

        dataframes = read_csv_files_in_folder(self.folder_path.get())
        num_files = len(dataframes)
        self.file_count_label.config(
            text=f"Serão processados {num_files} arquivos")
        self.execute_button.config(state=tk.NORMAL)

    # Função para executar o processamento dos dados
    def execute_processing(self):
        folder_path = self.folder_path.get()
        if not folder_path:
            messagebox.showerror("Erro", Messages.INPUT_ERROR_MESSAGE)
            return

        dataframes = read_csv_files_in_folder(self.folder_path.get())
        total_files = len(dataframes)
        self.progress['maximum'] = total_files
        self.progress['value'] = 0

        output_folder = os.path.join(folder_path, "output_climate2swat")
        os.makedirs(output_folder, exist_ok=True)

        for idx, (file_name, (df, name, code)) in enumerate(
                dataframes.items(), 1):
            df_filled = fill_missing_dates(df, date_col='Data Medicao')
            save_to_txt(df_filled, name, code, output_folder)
            self.saved_files.append(f"{name}_{code}.txt")

            self.progress['value'] = idx
            self.root.update()

        output_folder_path = os.path.abspath(output_folder)

        self.execute_button.config(state=tk.DISABLED)
        self.complete_message.config(
            text=f"Processamento concluído!\n\n"
            f"Os arquivos foram salvos na pasta:\n"
            f"{output_folder_path}")

        self.close_button.config(state=tk.NORMAL)
        messagebox.showinfo("Concluído", Messages.CLOSE_MESSAGE)


# Função para iniciar a aplicação
def main():
    root = tk.Tk()
    ProcessingApp(root)
    root.mainloop()


if __name__ == '__main__':
    main()
