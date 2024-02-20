import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("¬ведите количество строк в массиве:");
        int n = scanner.nextInt();
        scanner.nextLine(); // —читываем символ новой строки после ввода числа

        String[] strings = new String[n];

        System.out.println("¬ведите строки массива:");
        for (int i = 0; i < n; i++) {
            strings[i] = scanner.nextLine();
        }

        String[] result = filterStrings(strings);

        System.out.println("–езультат:");
        for (String str : result) {
            System.out.println(str);
        }
    }

    public static String[] filterStrings(String[] strings) {
        int count = 0;
        for (String str : strings) {
            if (str.length() <= 3) {
                count++;
            }
        }

        String[] result = new String[count];
        int index = 0;
        for (String str : strings) {
            if (str.length() <= 3) {
                result[index] = str;
                index++;
            }
        }

        return result;
    }
}