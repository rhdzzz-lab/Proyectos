import java.util.Scanner;

public class StringToolbox {

    private static String readNonEmpty(Scanner sc, String prompt) {
        String s;
        do {
            System.out.print(prompt);
            s = sc.nextLine();
        } while (s == null || s.isEmpty());
        return s;
    }

    private static int toIntOrDefault(String s, int def) {
        try { 
            return Integer.parseInt(s.trim()); 
        } catch (Exception e) { 
            return def; 
        }
    }

    private static String reverse(String s) {
        String r = "";
        for (int i = s.length() - 1; i >= 0; i--) {
            r = r + s.substring(i, i + 1);
        }
        return r;
    }

    private static int countOccurrences(String text, String sub) {
        if (sub.isEmpty()) return 0;
        return (text.length() - text.replace(sub, "").length()) / sub.length();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        try {
            System.out.println("=== Caja de Herramientas de String ===");
            System.out.println("Escribe tu cadena base y luego elige comandos por nombre.");
            String base = readNonEmpty(sc, "Cadena base: ");

            String ayuda =
                "\nComandos disponibles (escríbelos tal cual):\n" +
                "  longitud           -> muestra la longitud\n" +
                "  mayusculas         -> convierte a MAYÚSCULAS\n" +
                "  minusculas         -> convierte a minúsculas\n" +
                "  trim               -> quita espacios al inicio/fin\n" +
                "  reemplazar         -> reemplaza subcadenas\n" +
                "  subcadena          -> extrae substring [inicio, fin)\n" +
                "  contiene           -> verifica si contiene un texto\n" +
                "  empieza            -> verifica si empieza con...\n" +
                "  termina            -> verifica si termina con...\n" +
                "  indice             -> primer índice de un texto\n" +
                "  ultimoindice       -> último índice de un texto\n" +
                "  sinespacios        -> elimina TODOS los espacios\n" +
                "  contar             -> cuenta ocurrencias de un texto\n" +
                "  invertir           -> invierte la cadena\n" +
                "  iguala             -> compara con otra cadena (sensible)\n" +
                "  igualaignorar      -> compara ignorando mayúsc/minúsc\n" +
                "  nueva              -> cambia la cadena base\n" +
                "  ver                -> muestra la cadena base actual\n" +
                "  ayuda              -> muestra esta ayuda\n" +
                "  salir              -> termina el programa\n";

            System.out.println(ayuda);

            while (true) {
                try {
                    System.out.print("\nCadena actual => \"" + base + "\"\n> Comando: ");
                    String cmd = sc.nextLine().trim().toLowerCase();

                    if (cmd.equals("salir")) {
                        System.out.println("¡Adiós!");
                        break;
                    } else if (cmd.equals("ayuda")) {
                        System.out.println(ayuda);
                    } else if (cmd.equals("ver")) {
                        System.out.println("Cadena: \"" + base + "\"");
                    } else if (cmd.equals("longitud")) {
                        System.out.println("Longitud: " + base.length());
                    } else if (cmd.equals("mayusculas")) {
                        base = base.toUpperCase();
                        System.out.println("→ " + base);
                    } else if (cmd.equals("minusculas")) {
                        base = base.toLowerCase();
                        System.out.println("→ " + base);
                    } else if (cmd.equals("trim")) {
                        base = base.trim();
                        System.out.println("→ " + base);
                    } else if (cmd.equals("reemplazar")) {
                        String viejo = readNonEmpty(sc, "Texto a reemplazar: ");
                        String nuevo = readNonEmpty(sc, "Reemplazar por: ");
                        base = base.replace(viejo, nuevo);
                        System.out.println("→ " + base);
                    } else if (cmd.equals("subcadena")) {
                        String sinicio = readNonEmpty(sc, "Inicio (0..n): ");
                        String sfin    = readNonEmpty(sc, "Fin (<=n): ");
                        int ini = toIntOrDefault(sinicio, 0);
                        int fin = toIntOrDefault(sfin, base.length());
                        // Acotar a rangos válidos
                        ini = Math.max(0, Math.min(ini, base.length()));
                        fin = Math.max(ini, Math.min(fin, base.length()));
                        System.out.println("Subcadena [" + ini + "," + fin + "): \"" + base.substring(ini, fin) + "\"");
                    } else if (cmd.equals("contiene")) {
                        String sub = readNonEmpty(sc, "Texto a buscar: ");
                        System.out.println(base.contains(sub) ? "Sí contiene." : "No contiene.");
                    } else if (cmd.equals("empieza")) {
                        String pref = readNonEmpty(sc, "Prefijo: ");
                        System.out.println(base.startsWith(pref) ? "Sí empieza con ese prefijo." : "No empieza con ese prefijo.");
                    } else if (cmd.equals("termina")) {
                        String suf = readNonEmpty(sc, "Sufijo: ");
                        System.out.println(base.endsWith(suf) ? "Sí termina con ese sufijo." : "No termina con ese sufijo.");
                    } else if (cmd.equals("indice")) {
                        String sub = readNonEmpty(sc, "Texto: ");
                        System.out.println("Índice: " + base.indexOf(sub));
                    } else if (cmd.equals("ultimoindice")) {
                        String sub = readNonEmpty(sc, "Texto: ");
                        System.out.println("Último índice: " + base.lastIndexOf(sub));
                    } else if (cmd.equals("sinespacios")) {
                        base = base.replace(" ", "");
                        System.out.println("→ " + base);
                    } else if (cmd.equals("contar")) {
                        String sub = readNonEmpty(sc, "Subtexto a contar: ");
                        System.out.println("Ocurrencias: " + countOccurrences(base, sub));
                    } else if (cmd.equals("invertir")) {
                        base = reverse(base);
                        System.out.println("→ " + base);
                    } else if (cmd.equals("iguala")) {
                        String otra = readNonEmpty(sc, "Otra cadena: ");
                        System.out.println(base.equals(otra) ? "iguales" : "diferentes");
                    } else if (cmd.equals("igualaignorar")) {
                        String otra = readNonEmpty(sc, "Otra cadena: ");
                        System.out.println(base.equalsIgnoreCase(otra) ? "iguales (ignorando mayúsc/minúsc)" : "diferentes");
                    } else if (cmd.equals("nueva")) {
                        base = readNonEmpty(sc, "Nueva cadena base: ");
                    } else {
                        System.out.println("Comando no reconocido. Escribe 'ayuda' para ver opciones.");
                    }
                } catch (IndexOutOfBoundsException e) {
                    System.out.println("Error: índices fuera de rango. Verifica 'inicio' y 'fin' para 'subcadena'.");
                } catch (IllegalArgumentException e) {
                    System.out.println("Entrada inválida: " + e.getMessage());
                } catch (Exception e) {
                    System.out.println("Ocurrió un error y se continuará: " + e.getClass().getSimpleName() + " - " + e.getMessage());
                }
            }
        } finally {
            sc.close();
        }
    }
}
