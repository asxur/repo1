exam_points = {
  "Mariusz":30,
  "Mateusz":55,
  "Marta":76,
  "Roman":30,
  "Arleta":59,
  "Adrian": 96,
  "Monika":91,
  "Andrzej":22,
  "Krzysztof":83,
  "Krystyna":93,
  "Piotr":44,
  "Dawid":10,
  "Agnieszka":15
}

failed_students = [student for student, score in exam_points.items() if score < 45]
print(f"Studenci, ktorzy nie zdali testu to : {failed_students}")
top_students = [student for student, score in exam_points.items() if score > 90]
print(f"Studenci, ktorzy zdali test na BDB to : {top_students}")
best_student = sorted(exam_points.items())
print(f"Najlepszym studentem jest", best_student[0])
print(f"Zmiana 1")
print("Pozdro kolego")
