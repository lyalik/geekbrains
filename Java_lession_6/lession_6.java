import java.util.*;
// -*- coding: utf-8 -*-
class ������� {
    private String ������;
    private int ��������;
    private int �������;
    private String �������������������;
    private String ����;

    public �������(String ������, int ��������, int �������, String �������������������, String ����) {
        this.������ = ������;
        this.�������� = ��������;
        this.������� = �������;
        this.������������������� = �������������������;
        this.���� = ����;
    }

    public String get������() {
        return ������;
    }

    public int get��������() {
        return ��������;
    }

    public int get�������() {
        return �������;
    }

    public String get�������������������() {
        return �������������������;
    }

    public String get����() {
        return ����;
    }

    @Override
    public String toString() {
        return "\u041D\u043E\u0443\u0442\u0431\u0443\u043A{" +
                "������='" + ������ + '\'' +
                ", ��������=" + �������� +
                ", �������=" + ������� +
                ", �������������������='" + ������������������� + '\'' +
                ", ����='" + ���� + '\'' +
                '}';
    }
}

public class Main {
    public static void main(String[] args) {
        Set<�������> �������� = new HashSet<>();
        ��������.add(new �������("������� 1", 8, 512, "Windows 10", "������"));
        ��������.add(new �������("������� 2", 16, 1024, "Windows 10", "�����������"));
        ��������.add(new �������("������� 3", 8, 256, "MacOS", "�����"));
        ��������.add(new �������("������� 4", 16, 512, "Windows 10", "������"));
        ��������.add(new �������("������� 5", 8, 512, "Windows 10", "�����������"));

        Map<Integer, String> �������� = new HashMap<>();
        ��������.put(1, "��������");
        ��������.put(2, "�������");
        ��������.put(3, "�������������������");
        ��������.put(4, "����");

        Scanner scanner = new Scanner(System.in);
        System.out.println("������� �����, ��������������� ������������ ��������:");
        System.out.println("1 - ���");
        System.out.println("2 - ����� ��");
        System.out.println("3 - ������������ �������");
        System.out.println("4 - ����");
        int ����������������� = scanner.nextInt();
        String �������� = ��������.get(�����������������);

        System.out.println("������� ����������� �������� ��� ���������� ��������:");
        int ������������������� = scanner.nextInt();

        Set<�������> ����������������������� = new HashSet<>();
        for (������� ������� : ��������) {
            switch (��������) {
                case "��������":
                    if (�������.get��������() >= �������������������) {
                        �����������������������.add(�������);
                    }
                    break;
                case "�������":
                    if (�������.get�������() >= �������������������) {
                        �����������������������.add(�������);
                    }
                    break;
                case "�������������������":
                    if (�������.get�������������������().equals(String.valueOf(�������������������))) {
                        �����������������������.add(�������);
                    }
                    break;
                case "����":
                    if (�������.get����().equals(String.valueOf(�������������������))) {
                        �����������������������.add(�������);
                    }
                    break;
            }
        }

        System.out.println("��������������� ��������:");
        for (������� ������� : �����������������������) {
            System.out.println(�������);
        }
    }
}