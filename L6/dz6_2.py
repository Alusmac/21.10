# Ваше завдання — написати програму
# яка переводить число у формат часу у читальному вигляді.
seconds = int(input("Введіть кількість секунд: "))

days, ostat = divmod(seconds, 86400)
hours, ostat = divmod(ostat, 3600)
minutes, seconds = divmod(ostat, 60)

print(f"{days} днів, {hours:02}:{minutes:02}:{seconds:02}")
