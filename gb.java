java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Ввод массива строк с клавиатуры
        System.out.println("Введите количество строк в массиве:");
        int n = scanner.nextInt();
        scanner.nextLine(); // Потребление новой строки после nextInt()

        String[] inputArray = new String[n];
        System.out.println("Введите строки:");
        for (int i = 0; i < n; i++) {
            inputArray[i] = scanner.nextLine();
        }

        // Формирование нового массива
        String[] resultArray = filterShortStrings(inputArray);

        // Вывод результата
        System.out.println("Новый массив строк, длина которых <= 3 символам:");
        for (String str : resultArray) {
            System.out.println(str);
        }
    }

    public static String[] filterShortStrings(String[] array) {
        int count = 0;

        // Подсчет количества строк, длина которых <= 3 символам
        for (String str : array) {
            if (str.length() <= 3) {
                count++;
            }
        }

        // Создание нового массива нужного размера
        String[] result = new String[count];
        int index = 0;

        // Заполнение нового массива
        for (String str : array) {
            if (str.length() <= 3) {
                result[index++] = str;
            }
        }

        return result;
    }
}
