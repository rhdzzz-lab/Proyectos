import java.util.*;

public class Practica12 {

    private static final Scanner SC = new Scanner(System.in);

    public static void main(String[] args) {
        System.out.println("=== DEMO DE MÉTODOS String ===");
        String base = readNonEmpty("Ingresa una cadena base: ");

        while (true) {
            System.out.println("\n--- MENÚ ---");
            System.out.println("1) contains");
            System.out.println("2) split");
            System.out.println("3) equals");
            System.out.println("4) equalsIgnoreCase");
            System.out.println("5) endsWith");
            System.out.println("6) join");
            System.out.println("7) replace");
            System.out.println("8) startsWith");
            System.out.println("9) trim");
            System.out.println("10) concat");
            System.out.println("0) Salir");

            int op = readIntInRange("Elige opción: ", 0, 10);
            if (op == 0) {
                System.out.println("¡Listo! Hasta luego.");
                break;
            }

            switch (op) {
                case 1 -> demoContains(base);
                case 2 -> base = demoSplit(base);
                case 3 -> demoEquals(base);
                case 4 -> demoEqualsIgnoreCase(base);
                case 5 -> demoEndsWith(base);
                case 6 -> demoJoin();
                case 7 -> base = demoReplace(base);
                case 8 -> demoStartsWith(base);
                case 9 -> base = demoTrim(base);
                case 10 -> base = demoConcat(base);
            }
        }
    }


    private static void demoContains(String base) {
        String sub = readNonEmpty("Subcadena a buscar con contains: ");
        boolean ok = base.contains(sub);
        System.out.println("Resultado: \"" + base + "\".contains(\"" + sub + "\") = " + ok);
    }

    private static String demoSplit(String base) {
        String regex = readNonEmpty("Regex/separador para split (p.ej. \",\" o \"\\s+\"): ");
        String limitStr = readOptional("Límite (Enter para sin límite): ");
        String[] partes;
        if (limitStr.isEmpty()) {
            partes = base.split(regex);
        } else {
            int limit = safeParseInt(limitStr, 0);
            partes = base.split(regex, limit);
        }
        System.out.println("Partes (" + partes.length + "): " + Arrays.toString(partes));
        return base;
    }

    private static void demoEquals(String base) {
    String otra = readNonEmpty("Cadena a comparar con equals: ");
    System.out.println("equals      = " + base.equals(otra));
}

    private static void demoEqualsIgnoreCase(String base) {
        String otra = readNonEmpty("Cadena a comparar con equalsIgnoreCase: ");
        boolean eq = base.equalsIgnoreCase(otra);
        System.out.println("Resultado: \"" + base + "\".equalsIgnoreCase(\"" + otra + "\") = " + eq);
    }

    private static void demoEndsWith(String base) {
        String suf = readNonEmpty("Sufijo para endsWith: ");
        boolean ok = base.endsWith(suf);
        System.out.println("Resultado: \"" + base + "\".endsWith(\"" + suf + "\") = " + ok);
    }

    private static void demoJoin() {
        int n = readIntInRange("¿Cuántos elementos vas a unir con join? ", 0, 1000);
        List<String> elems = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            elems.add(readNonEmpty("Elemento " + i + ": "));
        }
        String delim = readNonEmpty("Delimitador: ");
        String unido = String.join(delim, elems);
        System.out.println("String.join -> " + unido);
    }

    private static String demoReplace(String base) {
        String target = readNonEmpty("Texto a reemplazar (target) para replace: ");
        String repl = readNonEmpty("Reemplazo (replacement): ");
        String nuevo = base.replace(target, repl);
        System.out.println("Resultado: " + nuevo);
        return nuevo;
    }

    private static void demoStartsWith(String base) {
        String pref = readNonEmpty("Prefijo para startsWith: ");
        boolean ok = base.startsWith(pref);
        System.out.println("Resultado: \"" + base + "\".startsWith(\"" + pref + "\") = " + ok);
    }

    private static String demoTrim(String base) {
        String tr = base.trim();
        System.out.println("Antes (len=" + base.length() + "): «" + base + "»");
        System.out.println("Después (len=" + tr.length() + "): «" + tr + "»");
        return tr;
    }

    private static String demoConcat(String base) {
        String extra = readNonEmpty("Texto a concatenar con concat: ");
        String res = base.concat(extra);
        System.out.println("Resultado: " + res);
        return res;
    }


    private static String readNonEmpty(String prompt) {
        String s;
        do {
            System.out.print(prompt);
            s = SC.nextLine();
            if (s == null) s = "";
        } while (s.isEmpty());
        return s;
    }

    private static String readOptional(String prompt) {
        System.out.print(prompt);
        String s = SC.nextLine();
        return (s == null) ? "" : s;
    }

    private static int readIntInRange(String prompt, int min, int max) {
        while (true) {
            System.out.print(prompt);
            String raw = SC.nextLine();
            try {
                int v = Integer.parseInt(raw.trim());
                if (v < min || v > max) {
                    System.out.println("Debe estar entre " + min + " y " + max + ".");
                    continue;
                }
                return v;
            } catch (NumberFormatException e) {
                System.out.println("Ingresa un número válido.");
            }
        }
    }

    private static int safeParseInt(String s, int def) {
        try { return Integer.parseInt(s.trim()); } catch (Exception e) { return def; }
    }
}
