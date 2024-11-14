import matplotlib.pyplot as plt

# Sample data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown']


plt.bar(languages, popularity, color=colors)

plt.xlabel('Programming Languages')
plt.ylabel('Popularity (%)')
plt.title('Popularity of Programming Languages')

plt.xticks(rotation=45)  
plt.tight_layout()  
plt.show()
