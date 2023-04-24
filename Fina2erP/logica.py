from tkinter import messagebox
import re

class RomanArabicConverter:
   
    def roman_to_arabic(self, roman_num):
        roman_dict = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50}
        arabic_num = 0
        roman_num = roman_num.upper()
        
        if roman_num == "":
            messagebox.showerror("Error", "El campo esta vacio")
            return

        try:
            if roman_num[0] == 'L' and roman_num[1] in roman_dict:
                messagebox.showerror("Error", "El número romano es mayor a 50")
                return
        except:
            pass
        # Verificar que no se repitan más de tres veces seguidas los caracteres 
        if re.search('I{4,}|X{4,}', roman_num):
            messagebox.showerror("Error", "El número romano contiene patrones de caracteres inválidos")
            return

        # Verificar que no se usen combinaciones inválidas
        invalid_combinations = ['VX', 'VL']
        if any(substring in roman_num for substring in invalid_combinations):
            messagebox.showerror("Error", "El número romano contiene combinaciones inválidas")
            return
        
        
        for key in sorted(roman_dict, reverse=True):
            while roman_num[0:len(key)] == key:
                arabic_num += roman_dict[key]
                roman_num = roman_num[len(key):]
        
        if arabic_num > 50 or arabic_num == 0:
            messagebox.showerror("Error", "El número romano es inválido o mayor a 50")
            return
        messagebox.showinfo("Resultado", "El número romano a arábigo es: " + str(arabic_num))

    def arabic_to_roman(self, arabic_num):
        roman_dict = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L"}
        roman_num = ""
      
        try:
            if int(arabic_num) > 50:
                messagebox.showerror("Error", "El número arábigo es mayor a 50")
                return
        except:
            pass

        for key in sorted(roman_dict, reverse=True):
            while arabic_num >= key:
                roman_num += roman_dict[key]
                arabic_num -= key
        messagebox.showinfo("Resultado", "El número arábigo a romano es: " + str(roman_num))