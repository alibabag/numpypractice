import matplotlib.pyplot as plt


yil = [2011, 2012, 2013, 2014, 2015]

oyuncu1 = [8, 10, 12, 7, 9]
oyuncu2 = [7, 12, 5, 15, 21]
oyuncu3 = [10, 9, 11, 6, 13]


#Stack plot
'''
plt.plot([], [], color='m', label='Oyuncu 1')
plt.plot([], [], color='c', label='Oyuncu 2')
plt.plot([], [], color='r', label='Oyuncu 3')

plt.stackplot(yil, oyuncu1, oyuncu2, oyuncu3, colors=['m', 'c', 'r'])

#ayrı ayrı plot yapmamıza gerek kalmadı
plt.title('Yıllara Göre Oyuncu Skorları')
plt.xlabel('Yıl')
plt.ylabel('Skor')

plt.legend()
plt.show()

#üst üste kapladığı alanı gösterdi
'''
'''
Pie grafik
goal_types = ['Penaltı', 'Serbest Vuruş', 'Kaleye Atış', 'Kafa', 'Korner']
goals = [12, 5, 3, 7, 2]
colors = ['r', 'g', 'b', 'y', 'c']
plt.pie(goals, labels=goal_types, colors=colors, startangle=90, shadow=True, explode=(0, 0, 0.1, 0, 0), autopct='%1.1f%%')#explode ile bir dilim dışarı çıkarıldı


plt.show()
'''


'''
Bar grafik
plt.bar([0.25, 1.25, 2.25, 3.25, 4.25], [50, 40, 70, 80, 20],label='BMW', width=0.5)
plt.bar([0.75, 1.75, 2.75, 3.75, 4.75], [80, 20, 20, 50, 60],label='Audi', width=0.5)

plt.legend()
plt.xlabel('Gün')
plt.ylabel('Mesafe (km)')
plt.title('Araç Bilgileri')
plt.show()
'''

#histogram grafiği
yaslar = [22, 55, 62, 45, 21, 22, 34, 42, 42, 4, 99, 101, 120, 122, 130]
yas_gruplari = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]

plt.hist(yaslar, yas_gruplari, histtype='bar', rwidth=0.8)
plt.xlabel('Yaş Grupları')
plt.ylabel('Kişi Sayısı')
plt.title('Histogram Grafiği')
plt.show()
