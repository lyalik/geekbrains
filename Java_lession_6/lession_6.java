import java.util.*;
// -*- coding: utf-8 -*-
class Ноутбук {
    private String модель;
    private int объемОЗУ;
    private int объемЖД;
    private String операционнаяСистема;
    private String цвет;

    public Ноутбук(String модель, int объемОЗУ, int объемЖД, String операционнаяСистема, String цвет) {
        this.модель = модель;
        this.объемОЗУ = объемОЗУ;
        this.объемЖД = объемЖД;
        this.операционнаяСистема = операционнаяСистема;
        this.цвет = цвет;
    }

    public String getМодель() {
        return модель;
    }

    public int getОбъемОЗУ() {
        return объемОЗУ;
    }

    public int getОбъемЖД() {
        return объемЖД;
    }

    public String getОперационнаяСистема() {
        return операционнаяСистема;
    }

    public String getЦвет() {
        return цвет;
    }

    @Override
    public String toString() {
        return "\u041D\u043E\u0443\u0442\u0431\u0443\u043A{" +
                "модель='" + модель + '\'' +
                ", объемОЗУ=" + объемОЗУ +
                ", объемЖД=" + объемЖД +
                ", операционнаяСистема='" + операционнаяСистема + '\'' +
                ", цвет='" + цвет + '\'' +
                '}';
    }
}

public class Main {
    public static void main(String[] args) {
        Set<Ноутбук> ноутбуки = new HashSet<>();
        ноутбуки.add(new Ноутбук("Ноутбук 1", 8, 512, "Windows 10", "Черный"));
        ноутбуки.add(new Ноутбук("Ноутбук 2", 16, 1024, "Windows 10", "Серебристый"));
        ноутбуки.add(new Ноутбук("Ноутбук 3", 8, 256, "MacOS", "Серый"));
        ноутбуки.add(new Ноутбук("Ноутбук 4", 16, 512, "Windows 10", "Черный"));
        ноутбуки.add(new Ноутбук("Ноутбук 5", 8, 512, "Windows 10", "Серебристый"));

        Map<Integer, String> критерии = new HashMap<>();
        критерии.put(1, "объемОЗУ");
        критерии.put(2, "объемЖД");
        критерии.put(3, "операционнаяСистема");
        критерии.put(4, "цвет");

        Scanner scanner = new Scanner(System.in);
        System.out.println("Введите цифру, соответствующую необходимому критерию:");
        System.out.println("1 - ОЗУ");
        System.out.println("2 - Объем ЖД");
        System.out.println("3 - Операционная система");
        System.out.println("4 - Цвет");
        int выбранныйКритерий = scanner.nextInt();
        String критерий = критерии.get(выбранныйКритерий);

        System.out.println("Введите минимальное значение для выбранного критерия:");
        int минимальноеЗначение = scanner.nextInt();

        Set<Ноутбук> отфильтрованныеНоутбуки = new HashSet<>();
        for (Ноутбук ноутбук : ноутбуки) {
            switch (критерий) {
                case "объемОЗУ":
                    if (ноутбук.getОбъемОЗУ() >= минимальноеЗначение) {
                        отфильтрованныеНоутбуки.add(ноутбук);
                    }
                    break;
                case "объемЖД":
                    if (ноутбук.getОбъемЖД() >= минимальноеЗначение) {
                        отфильтрованныеНоутбуки.add(ноутбук);
                    }
                    break;
                case "операционнаяСистема":
                    if (ноутбук.getОперационнаяСистема().equals(String.valueOf(минимальноеЗначение))) {
                        отфильтрованныеНоутбуки.add(ноутбук);
                    }
                    break;
                case "цвет":
                    if (ноутбук.getЦвет().equals(String.valueOf(минимальноеЗначение))) {
                        отфильтрованныеНоутбуки.add(ноутбук);
                    }
                    break;
            }
        }

        System.out.println("Отфильтрованные ноутбуки:");
        for (Ноутбук ноутбук : отфильтрованныеНоутбуки) {
            System.out.println(ноутбук);
        }
    }
}