import java.util.Scanner;

public class nintedo {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.println("¿De qué modelo de Nintendo Switch quieres saber? (Estandar, Lite, Oled): ");
            String opcion = scanner.nextLine().trim().toLowerCase();

            switch (opcion) {
                case "estandar" -> {
                    Estandar estandar = new Estandar();
                    // Valores de ejemplo
                    estandar.setCpu("NVIDIA Custom Tegra");
                    estandar.setGpu("NVIDIA GM20B Maxwell");
                    estandar.setRam(4);
                    estandar.setAlmacenamientoInterno(32);
                    estandar.setConectividad("WiFi, Bluetooth");
                    estandar.setPantallaTipo("LCD");
                    estandar.setPantallaTamano(6.2f);
                    estandar.setResolucion("1280x720");
                    estandar.setControlesRemovibles(true);
                    estandar.setSoporteTrasero("Simple");
                    System.out.println("Seleccionaste Nintendo Switch Estándar.");
                    estandar.ponerEnModoTV();
                    estandar.desmontarJoyCon();
                    System.out.println("CPU (String): " + estandar.getCpu());
                    System.out.println("GPU (String): " + estandar.getGpu());
                    System.out.println("RAM (int): " + estandar.getRam() + " GB");
                    System.out.println("Almacenamiento (int): " + estandar.getAlmacenamientoInterno() + " GB");
                    System.out.println("Conectividad (String): " + estandar.getConectividad());
                    System.out.println("PantallaTipo (String): " + estandar.getPantallaTipo());
                    System.out.println("PantallaTamano (float): " + estandar.getPantallaTamano() + " pulgadas");
                    System.out.println("Resolución (String): " + estandar.getResolucion());
                    System.out.println("Controles removibles (boolean): " + estandar.isControlesRemovibles());
                    System.out.println("Soporte trasero (String): " + estandar.getSoporteTrasero());
                }
                case "lite" -> {
                    Lite lite = new Lite();
                    // Valores de ejemplo
                    lite.setCpu("NVIDIA Custom Tegra");
                    lite.setGpu("NVIDIA GM20B Maxwell");
                    lite.setRam(4);
                    lite.setAlmacenamientoInterno(32);
                    lite.setConectividad("WiFi, Bluetooth");
                    lite.setPantallaTipo("LCD");
                    lite.setPantallaTamano(5.5f);
                    lite.setResolucion("1280x720");
                    lite.setVibracionHD(false);
                    System.out.println("Seleccionaste Nintendo Switch Lite.");
                    lite.calibrarPalancasIntegradas();
                    lite.activarBluetoothParaAudifonos();
                    System.out.println("CPU (String): " + lite.getCpu());
                    System.out.println("GPU (String): " + lite.getGpu());
                    System.out.println("RAM (int): " + lite.getRam() + " GB");
                    System.out.println("Almacenamiento (int): " + lite.getAlmacenamientoInterno() + " GB");
                    System.out.println("Conectividad (String): " + lite.getConectividad());
                    System.out.println("PantallaTipo (String): " + lite.getPantallaTipo());
                    System.out.println("PantallaTamano (float): " + lite.getPantallaTamano() + " pulgadas");
                    System.out.println("Resolución (String): " + lite.getResolucion());
                    System.out.println("Vibración HD (boolean): " + lite.isVibracionHD());
                }
                case "oled" -> {
                    System.out.println("¿De qué versión OLED quieres saber? (Normal, EdicionEspecial, Zelda): ");
                    String subopcion = scanner.nextLine().trim().toLowerCase();
                    switch (subopcion) {
                        case "norma", "normal" -> {
                            Oled oled = new Oled();
                            oled.setCpu("NVIDIA Custom Tegra");
                            oled.setGpu("NVIDIA GM20B Maxwell");
                            oled.setRam(4);
                            oled.setAlmacenamientoInterno(64);
                            oled.setConectividad("WiFi, Bluetooth, Ethernet");
                            oled.setPantallaTipo("OLED");
                            oled.setPantallaTamano(7.0f);
                            oled.setResolucion("1280x720");
                            oled.setSoporteTrasero("Ajustable");
                            oled.setPuertoEthernet(true);
                            System.out.println("Seleccionaste Nintendo Switch OLED Normal.");
                            oled.activarModoColoresVivos();
                            oled.usarSoporteAjustable();
                            System.out.println("CPU (String): " + oled.getCpu());
                            System.out.println("GPU (String): " + oled.getGpu());
                            System.out.println("RAM (int): " + oled.getRam() + " GB");
                            System.out.println("Almacenamiento (int): " + oled.getAlmacenamientoInterno() + " GB");
                            System.out.println("Conectividad (String): " + oled.getConectividad());
                            System.out.println("PantallaTipo (String): " + oled.getPantallaTipo());
                            System.out.println("PantallaTamano (float): " + oled.getPantallaTamano() + " pulgadas");
                            System.out.println("Resolución (String): " + oled.getResolucion());
                            System.out.println("Soporte trasero (String): " + oled.getSoporteTrasero());
                            System.out.println("Puerto Ethernet (boolean): " + oled.isPuertoEthernet());
                        }
                        case "edicionespecial", "especial" -> {
                            OledEdicionEspecial especial = new OledEdicionEspecial();
                            // Asignar valores heredados
                            especial.setCpu("NVIDIA Custom Tegra");
                            especial.setGpu("NVIDIA GM20B Maxwell");
                            especial.setRam(4);
                            especial.setAlmacenamientoInterno(64);
                            especial.setConectividad("WiFi, Bluetooth, Ethernet");
                            especial.setPantallaTipo("OLED");
                            especial.setPantallaTamano(7.0f);
                            especial.setResolucion("1280x720");
                            especial.setSoporteTrasero("Ajustable");
                            especial.setPuertoEthernet(true);
                            especial.mostrarTematica();
                        }
                        case "zelda" -> {
                            OledZelda zelda = new OledZelda();
                            // Asignar valores heredados
                            zelda.setCpu("NVIDIA Custom Tegra");
                            zelda.setGpu("NVIDIA GM20B Maxwell");
                            zelda.setRam(4);
                            zelda.setAlmacenamientoInterno(64);
                            zelda.setConectividad("WiFi, Bluetooth, Ethernet");
                            zelda.setPantallaTipo("OLED");
                            zelda.setPantallaTamano(7.0f);
                            zelda.setResolucion("1280x720");
                            zelda.setSoporteTrasero("Ajustable");
                            zelda.setPuertoEthernet(true);
                            zelda.mostrarEdicionZelda();
                        }
                        default -> System.out.println("Opción de OLED no válida. Intenta con: Normal, EdicionEspecial o Zelda.");
                    }
                }
                default -> System.out.println("Opción no válida. Intenta con: Estandar, Lite u Oled.");
            }

            // Las instancias de OledEdicionEspecial y OledZelda ahora se crean solo si el usuario lo pide
        }
    }
}

class NintendoSwitch {
    protected String cpu;
    protected String gpu;
    protected int ram;
    protected int almacenamientoInterno;
    protected String conectividad;
    protected String pantallaTipo;
    protected float pantallaTamano;
    protected String resolucion;

    // Constructor vacío
    public NintendoSwitch() {}

    // Constructor con parámetros
    public NintendoSwitch(String cpu, String gpu, int ram, int almacenamientoInterno, String conectividad, String pantallaTipo, float pantallaTamano, String resolucion) {
        this.cpu = cpu;
        this.gpu = gpu;
        this.ram = ram;
        this.almacenamientoInterno = almacenamientoInterno;
        this.conectividad = conectividad;
        this.pantallaTipo = pantallaTipo;
        this.pantallaTamano = pantallaTamano;
        this.resolucion = resolucion;
    }

    //GETTERS AND SETTERS
    public String getCpu(){return cpu;}
    public void setCpu(String cpu){this.cpu = cpu;}

    public String getGpu(){return gpu;}
    public void setGpu(String gpu){this.gpu = gpu;}

    public int getRam(){return ram;}
    public void setRam(int ram){this.ram = ram;}

    public int getAlmacenamientoInterno(){return almacenamientoInterno;}
    public void setAlmacenamientoInterno(int almacenamientoInterno){this.almacenamientoInterno = almacenamientoInterno;}

    public String getConectividad(){return conectividad;}
    public void setConectividad(String conectividad){this.conectividad = conectividad;}

    public String getPantallaTipo() { return pantallaTipo; }
    public void setPantallaTipo(String pantallaTipo) { this.pantallaTipo = pantallaTipo; }

    public float getPantallaTamano() { return pantallaTamano; }
    public void setPantallaTamano(float pantallaTamano) { this.pantallaTamano = pantallaTamano; }

    public String getResolucion() { return resolucion; }
    public void setResolucion(String resolucion) { this.resolucion = resolucion; }

    // Métodos
    public String iniciarJuego() {
        return "Iniciando juego...";
    }

    public void actualizarSoftware() {
        System.out.println("Actualizando software...");
    }

    public String conectarRed() {
        return "Conectando a la red...";
    }

    public void getDuracionBateria() {
        System.out.println("La duración de la batería es de 8 horas.");
    }
}

// Clase hija: Estándar
class Estandar extends NintendoSwitch {
    private boolean controlesRemovibles;
    private String soporteTrasero;

    public void ponerEnModoTV() {
        System.out.println("Modo TV activado.");
    }

    public void desmontarJoyCon() {
        System.out.println("Joy-Con desmontado.");
    }

    // Getters y setters
    public boolean isControlesRemovibles() { return controlesRemovibles; }
    public void setControlesRemovibles(boolean controlesRemovibles) { this.controlesRemovibles = controlesRemovibles; }
    public String getSoporteTrasero() { return soporteTrasero; }
    public void setSoporteTrasero(String soporteTrasero) { this.soporteTrasero = soporteTrasero; }
}

// Clase hija: Lite
class Lite extends NintendoSwitch {
    private boolean vibracionHD;

    public void calibrarPalancasIntegradas() {
        System.out.println("Calibrando palancas integradas...");
    }

    public void activarBluetoothParaAudifonos() {
        System.out.println("Bluetooth para audífonos activado.");
    }

    // Getters y setters
    public boolean isVibracionHD() { return vibracionHD; }
    public void setVibracionHD(boolean vibracionHD) { this.vibracionHD = vibracionHD; }
}

// Clase hija: OLED
class Oled extends NintendoSwitch {
    private String soporteTrasero;
    private boolean puertoEthernet;

    public Oled() { super(); }

    public Oled(String cpu, String gpu, int ram, int almacenamientoInterno, String conectividad, String pantallaTipo, float pantallaTamano, String resolucion, String soporteTrasero, boolean puertoEthernet) {
        super(cpu, gpu, ram, almacenamientoInterno, conectividad, pantallaTipo, pantallaTamano, resolucion);
        this.soporteTrasero = soporteTrasero;
        this.puertoEthernet = puertoEthernet;
    }

    public void activarModoColoresVivos() {
        System.out.println("Modo de colores vivos activado.");
    }

    public void usarSoporteAjustable() {
        System.out.println("Soporte ajustable en uso.");
    }

    // Getters y setters
    public String getSoporteTrasero() { return soporteTrasero; }
    public void setSoporteTrasero(String soporteTrasero) { this.soporteTrasero = soporteTrasero; }
    public boolean isPuertoEthernet() { return puertoEthernet; }
    public void setPuertoEthernet(boolean puertoEthernet) { this.puertoEthernet = puertoEthernet; }
}

// Clase nieta: OledEdicionEspecial
class OledEdicionEspecial extends Oled {
    private String tematica;
    private String colorEdicion;
    private boolean incluyeFunda;

    public OledEdicionEspecial() {
        super(
            "NVIDIA Custom Tegra",
            "NVIDIA GM20B Maxwell",
            4,
            64,
            "WiFi, Bluetooth, Ethernet",
            "OLED",
            7.0f,
            "1280x720",
            "Ajustable",
            true
        );
        this.tematica = "Edición especial";
        this.colorEdicion = "Rojo y azul";
        this.incluyeFunda = true;
    }

    public void mostrarTematica() {
        System.out.println("Esta es una Nintendo Switch OLED de temática: " + tematica);
        System.out.println("Color de la edición: " + colorEdicion);
        System.out.println("¿Incluye funda?: " + incluyeFunda);
        // Atributos heredados de Oled
        System.out.println("Soporte trasero (String): " + getSoporteTrasero());
        System.out.println("Puerto Ethernet (boolean): " + isPuertoEthernet());
        // Atributos heredados de NintendoSwitch
        System.out.println("CPU (String): " + getCpu());
        System.out.println("GPU (String): " + getGpu());
        System.out.println("RAM (int): " + getRam() + " GB");
        System.out.println("Almacenamiento (int): " + getAlmacenamientoInterno() + " GB");
        System.out.println("Conectividad (String): " + getConectividad());
        System.out.println("PantallaTipo (String): " + getPantallaTipo());
        System.out.println("PantallaTamano (float): " + getPantallaTamano() + " pulgadas");
        System.out.println("Resolución (String): " + getResolucion());
    }

    public String getTematica() { return tematica; }
    public void setTematica(String tematica) { this.tematica = tematica; }
    public String getColorEdicion() { return colorEdicion; }
    public void setColorEdicion(String colorEdicion) { this.colorEdicion = colorEdicion; }
    public boolean isIncluyeFunda() { return incluyeFunda; }
    public void setIncluyeFunda(boolean incluyeFunda) { this.incluyeFunda = incluyeFunda; }
}

// Clase nieta: OledZelda
class OledZelda extends Oled {
    private boolean incluyeJuegoZelda;
    private String arteJoyCon;
    private String versionJuego;

    public OledZelda() {
        super(
            "NVIDIA Custom Tegra",
            "NVIDIA GM20B Maxwell",
            4,
            64,
            "WiFi, Bluetooth, Ethernet",
            "OLED",
            7.0f,
            "1280x720",
            "Ajustable",
            true
        );
        this.incluyeJuegoZelda = true;
        this.arteJoyCon = "Diseño dorado con símbolos de Zelda";
        this.versionJuego = "Tears of the Kingdom";
    }

    public void mostrarEdicionZelda() {
        System.out.println("Esta es la edición OLED Zelda. ¿Incluye juego?: " + incluyeJuegoZelda);
        System.out.println("Arte especial en Joy-Con: " + arteJoyCon);
        System.out.println("Versión del juego incluida: " + versionJuego);
        // Atributos heredados de Oled
        System.out.println("Soporte trasero (String): " + getSoporteTrasero());
        System.out.println("Puerto Ethernet (boolean): " + isPuertoEthernet());
        // Atributos heredados de NintendoSwitch
        System.out.println("CPU (String): " + getCpu());
        System.out.println("GPU (String): " + getGpu());
        System.out.println("RAM (int): " + getRam() + " GB");
        System.out.println("Almacenamiento (int): " + getAlmacenamientoInterno() + " GB");
        System.out.println("Conectividad (String): " + getConectividad());
        System.out.println("PantallaTipo (String): " + getPantallaTipo());
        System.out.println("PantallaTamano (float): " + getPantallaTamano() + " pulgadas");
        System.out.println("Resolución (String): " + getResolucion());
    }

    public boolean isIncluyeJuegoZelda() { return incluyeJuegoZelda; }
    public void setIncluyeJuegoZelda(boolean incluyeJuegoZelda) { this.incluyeJuegoZelda = incluyeJuegoZelda; }
    public String getArteJoyCon() { return arteJoyCon; }
    public void setArteJoyCon(String arteJoyCon) { this.arteJoyCon = arteJoyCon; }
    public String getVersionJuego() { return versionJuego; }
    public void setVersionJuego(String versionJuego) { this.versionJuego = versionJuego; }
}