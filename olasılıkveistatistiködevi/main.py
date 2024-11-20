import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Rastgele veri oluşturma
np.random.seed(42)  # Tekrarlanabilir sonuçlar için sabit rastgelelik
a_firma_verileri = np.random.randint(0, 81, 100)  # 0-80 arası, 100 sayı
b_firma_verileri = np.random.randint(0, 81, 100)

# İstatistiksel Özellikler Fonksiyonu
def statistics(data):
    stats = {
        'Ortalama': np.mean(data),
        'Medyan': np.median(data),
        'Dağılım Genişliği': np.ptp(data),  # max - min
        'Varyans': np.var(data, ddof=1),  # örnek varyansı
        'Standart Sapma': np.std(data, ddof=1),  # örnek standart sapma
        'Çarpıklık': skew(data),
        'Basıklık': kurtosis(data)
    }
    return stats

# A ve B firmalarının istatistikleri
a_firma_stats = statistics(a_firma_verileri)
b_firma_stats = statistics(b_firma_verileri)

# GUI Arayüzü
class StatisticsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Firma İstatistikleri")
        self.root.geometry("600x500")
        self.root.configure(bg='#6A0DAD')  # Mor arka plan rengi

        # Başlık
        label = tk.Label(self.root, text="A ve B Firmalarının İstatistiksel Özellikleri", font=("Arial", 14), bg='#6A0DAD', fg='#FFFFFF')
        label.pack(pady=10)

        # A ve B Firma istatistiklerini sayısal olarak göstermek
        self.create_stat_frame('A Firması', a_firma_stats, 0)
        self.create_stat_frame('B Firması', b_firma_stats, 200)

        # Butonlar
        self.create_buttons()

    def create_stat_frame(self, firm_name, stats, y_offset):
        frame = tk.Frame(self.root, bg='#6A0DAD')
        frame.place(x=10, y=y_offset)

        tk.Label(frame, text=f"{firm_name} İstatistikleri", font=("Arial", 12), bg='#6A0DAD', fg='#FFFFFF').grid(row=0, column=0, columnspan=2, pady=5)

        row = 1
        for key, value in stats.items():
            tk.Label(frame, text=key, font=("Arial", 10), bg='#6A0DAD', fg='#FFFFFF').grid(row=row, column=0, padx=10, pady=5)
            tk.Label(frame, text=f"{value:.2f}", font=("Arial", 10), bg='#6A0DAD', fg='#FFFFFF').grid(row=row, column=1, padx=10, pady=5)
            row += 1

    def create_buttons(self):
        # Histogram butonu
        histogram_button = tk.Button(self.root, text="Histogram", command=self.show_histogram, bg='#D83D8D', fg='#FFFFFF', font=("Arial", 10))
        histogram_button.pack(pady=10)

        # Boxplot butonu
        boxplot_button = tk.Button(self.root, text="Boxplot", command=self.show_boxplot, bg='#D83D8D', fg='#FFFFFF', font=("Arial", 10))
        boxplot_button.pack(pady=5)

        # Karşılaştırmalı Bar Grafik butonu
        bar_graph_button = tk.Button(self.root, text="Karşılaştırmalı Bar Grafik", command=self.show_bar_graph, bg='#D83D8D', fg='#FFFFFF', font=("Arial", 10))
        bar_graph_button.pack(pady=5)

    def show_histogram(self):
        # Histogram grafiği
        plt.figure(figsize=(10, 6))
        plt.hist(a_firma_verileri, bins=20, alpha=0.7, label='A Firması', color='purple')
        plt.hist(b_firma_verileri, bins=20, alpha=0.7, label='B Firması', color='pink')
        plt.title('A ve B Firmalarının Histogramı', fontsize=14, color='#6A0DAD')
        plt.legend()
        plt.show()

    def show_boxplot(self):
        # Boxplot grafiği
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=[a_firma_verileri, b_firma_verileri], palette=["purple", "pink"])
        plt.xticks([0, 1], ['A Firması', 'B Firması'])
        plt.title('A ve B Firmalarının Dağılımı (Boxplot)', fontsize=14, color='#6A0DAD')
        plt.show()

    def show_bar_graph(self):
        # Karşılaştırmalı bar grafiği
        stats = ['Ortalama', 'Medyan', 'Dağılım Genişliği', 'Varyans', 'Standart Sapma', 'Çarpıklık', 'Basıklık']
        a_values = [a_firma_stats[stat] for stat in stats]
        b_values = [b_firma_stats[stat] for stat in stats]

        x = np.arange(len(stats))  # x ekseni için istatistiksel kategoriler
        width = 0.35  # bar genişliği

        fig, ax = plt.subplots(figsize=(10, 6))
        rects1 = ax.bar(x - width / 2, a_values, width, label='A Firması', color='#6A0DAD')
        rects2 = ax.bar(x + width / 2, b_values, width, label='B Firması', color='#D83D8D')

        ax.set_ylabel('Değerler')
        ax.set_title('A ve B Firmalarının İstatistiksel Karşılaştırması', fontsize=14, color='#6A0DAD')
        ax.set_xticks(x)
        ax.set_xticklabels(stats, rotation=45, ha='right', fontsize=10, color='#6A0DAD')
        ax.legend()

        plt.tight_layout()
        plt.show()

# Ana pencereyi oluşturma ve başlatma
root = tk.Tk()
app = StatisticsApp(root)
root.mainloop()
