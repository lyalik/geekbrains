import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("������� ���������� ����� � �������:");
        int n = scanner.nextInt();
        scanner.nextLine(); // ��������� ������ ����� ������ ����� ����� �����

        String[] strings = new String[n];

        System.out.println("������� ������ �������:");
        for (int i = 0; i < n; i++) {
            strings[i] = scanner.nextLine();
        }

        String[] result = filterStrings(strings);

        System.out.println("���������:");
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