import java.util.Scanner;

// ================== CLASE BASE ==================
public class NintendoSwitchApp {
    protected String modelo = "Nintendo Switch (Genérica)";
    protected String cpu;
    protected String gpu;
    protected int ram;
    protected int almacenamientoInterno;
    protected String conectividad;
    protected String pantallaTipo;
    protected float pantallaTamano;
    protected String resolucion;

    public NintendoSwitchApp() {
        this("NVIDIA Custom Tegra","NVIDIA GM20B Maxwell",4,32,"WiFi, Bluetooth","LCD",6.2f,"1280x720");
    }
    public NintendoSwitchApp(String cpu,String gpu,int ram,int almacenamientoInterno,
                             String conectividad,String pantallaTipo,float pantallaTamano,String resolucion){
        this.cpu = (cpu==null||cpu.isBlank())? "NVIDIA Custom Tegra": cpu;
        this.gpu = (gpu==null||gpu.isBlank())? "NVIDIA GM20B Maxwell": gpu;
        this.ram = Math.max(ram,1);
        this.almacenamientoInterno = Math.max(almacenamientoInterno,16);
        this.conectividad = (conectividad==null||conectividad.isBlank())? "WiFi, Bluetooth": conectividad;
        this.pantallaTipo = (pantallaTipo==null||pantallaTipo.isBlank())? "LCD": pantallaTipo;
        this.pantallaTamano = (pantallaTamano<=0)? 6.2f: pantallaTamano;
        this.resolucion = (resolucion==null||resolucion.isBlank())? "1280x720": resolucion;
    }

    // Fábricas
    public static Estandar modeloEstandar(){ return new Estandar(); }
    public static Lite modeloLite(){ return new Lite(); }
    public static Oled modeloOLED(){ return new Oled(); }
    public static OledEdicionEspecial modeloEspecial(String t,String c,boolean f){ return new OledEdicionEspecial(t,c,f); }
    public static OledZelda modeloZelda(boolean inc,String arte,String ver){ return new OledZelda(inc,arte,ver); }

    public String getModelo(){ return modelo; }

    @Override public String toString(){
        return """
               --- %s ---
               CPU: %s
               GPU: %s
               RAM: %d GB
               Almacenamiento: %d GB
               Conectividad: %s
               Pantalla: %s de %.1f" a %s
               """.formatted(modelo,cpu,gpu,ram,almacenamientoInterno,conectividad,pantallaTipo,pantallaTamano,resolucion);
    }

    // -------- Sobrecargas --------
    public String iniciarJuego(){ return "Iniciando juego..."; }
    public String iniciarJuego(String titulo){ return "Iniciando \""+titulo+"\" en modo estándar..."; }
    public String iniciarJuego(String titulo,String perfil){
        String p=(perfil==null||perfil.isBlank())?"equilibrado":perfil;
        return "Iniciando \""+titulo+"\" con perfil: "+p+".";
    }
    public String iniciarJuego(String titulo,boolean online,String... dlcs){
        String msg="Iniciando \""+titulo+(online?"\" en línea":"\" sin conexión");
        if(dlcs!=null && dlcs.length>0) msg+=" + DLCs: "+String.join(", ",dlcs);
        return msg+".";
    }

    public void actualizarSoftware(){ System.out.println("Actualizando software..."); }
    public void actualizarSoftware(boolean forzar){
        System.out.println(forzar? "Forzando actualización completa..." : "Actualizando software...");
    }
    public void actualizarSoftware(String canal){
        String c=(canal==null||canal.isBlank())?"estable":canal.toLowerCase();
        if(!c.equals("estable") && !c.equals("beta") && !c.equals("preview")){
            System.out.println("Canal no válido: \""+canal+"\". Usando 'estable'.");
            c="estable";
        }
        System.out.println("Actualizando desde canal \""+c+"\"...");
    }

    public String conectarRed(){ return "Conectando a la red..."; }
    public String conectarRed(String ssid){
        if(ssid==null||ssid.isBlank()) return "Error: SSID vacío.";
        return "Conectando a la red \""+ssid+"\" (abierta)...";
    }
    public String conectarRed(String ssid,String password){
        if(ssid==null||ssid.isBlank()) return "Error: SSID vacío.";
        if(password==null||password.isBlank()) return "Error: contraseña vacía para \""+ssid+"\".";
        return "Conectando a \""+ssid+"\" con autenticación...";
    }
    public String conectarRed(String ssid,String password,boolean recordar){
        String base=conectarRed(ssid,password);
        return base.startsWith("Error")? base : base+(recordar? " Guardando credenciales.":" Sin guardar credenciales.");
    }

    public String getDuracionBateria(){ return "Duración aproximada: 8.0 h"; }
    public String getDuracionBateria(String perfil){
        double h; String p=(perfil==null? "": perfil.trim().toLowerCase());
        switch(p){ case "ahorro"->h=9.5; case "alto"->h=6.0; default->h=8.0; }
        if(p.isEmpty()) p="equilibrado";
        return "Batería estimada ("+p+"): "+h+" h";
    }
    public String getDuracionBateria(int brillo,boolean wifi,boolean bt,boolean docked){
        if(brillo<0||brillo>100) return "Error: el brillo debe estar entre 0 y 100.";
        double h=9.0 - brillo*0.02 - (wifi?0.5:0) - (bt?0.3:0) - (docked?2.0:0);
        if(h<2.0) h=2.0;
        return String.format("Batería estimada (brillo=%d%%, wifi=%s, bt=%s, dock=%s): %.1f h",
                brillo, wifi?"on":"off", bt?"on":"off", docked?"sí":"no", h);
    }

    // -------- Métodos específicos con validación por defecto --------
    protected void noDisponible(String q){ System.out.println("No disponible en "+getModelo()+": "+q+"."); }
    public void ponerEnModoTV(){ noDisponible("Modo TV / Dock"); }
    public void desmontarJoyCon(){ noDisponible("Desmontar Joy-Con"); }
    public void activarModoColoresVivos(){ noDisponible("Modo colores vivos (solo OLED)"); }
    public void usarSoporteAjustable(){ noDisponible("Soporte ajustable (solo OLED)"); }
    public void calibrarBotonesIntegrados(){ noDisponible("Calibrar botones integrados (Lite)"); }
    public void activarBluetoothParaAudifonos(){ noDisponible("Bluetooth para audífonos (Lite)"); }
    public void mostrarTematica(){ noDisponible("Mostrar edición especial (OLED)"); }
    public void mostrarEdicionZelda(){ noDisponible("Mostrar edición Zelda (OLED)"); }

    // ================== MAIN ==================
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        try{
            System.out.println("¿Qué consola quieres consultar?");
            System.out.println("1) Nintendo Switch ESTÁNDAR");
            System.out.println("2) Nintendo Switch OLED");
            System.out.println("3) Nintendo Switch LITE");
            System.out.println("4) Nintendo Switch OLED - Edición Especial");
            System.out.println("5) Nintendo Switch OLED - Edición Zelda");
            System.out.print("Elige opción [1-5]: ");
            int opConsola = leerEnteroSeguro(sc);

            NintendoSwitchApp sw = null;
            if(opConsola==1) sw = NintendoSwitchApp.modeloEstandar();
            else if(opConsola==2) sw = NintendoSwitchApp.modeloOLED();
            else if(opConsola==3) sw = NintendoSwitchApp.modeloLite();
            else if(opConsola==4) sw = NintendoSwitchApp.modeloEspecial("Mario","Rojo",true);
            else if(opConsola==5) sw = NintendoSwitchApp.modeloZelda(true,"Triforce dorado","Tears of the Kingdom");
            else{
                System.out.println("Opción no válida. Usando modelo ESTÁNDAR.");
                sw = NintendoSwitchApp.modeloEstandar();
            }

            System.out.println("\nHas elegido: " + sw.getModelo());

            int op;
            do{
                System.out.println("\n=== MENÚ ===");
                System.out.println("1) Ver especificaciones");
                System.out.println("2) Iniciar juego (sobrecargas)");
                System.out.println("3) Conectar a red (sobrecargas)");
                System.out.println("4) Actualizar software (sobrecargas)");
                System.out.println("5) Estimar duración de batería (sobrecargas)");
                System.out.println("6) Acciones específicas del modelo");
                System.out.println("0) Salir");
                System.out.print("Elige opción: ");
                op = leerEnteroSeguro(sc);

                if(op==1){
                    System.out.println(sw);
                }
                else if(op==2){
                    System.out.print("Título: "); String titulo=sc.nextLine();
                    System.out.print("Perfil (alto/equilibrado/ahorro) o vacío: ");
                    String perfil=sc.nextLine();
                    System.out.println(perfil.isBlank()? sw.iniciarJuego(titulo) : sw.iniciarJuego(titulo,perfil));
                    System.out.print("¿Jugar en línea? (s/n): "); boolean online=leerSiNo(sc);
                    System.out.print("DLCs por coma (o vacío): "); String dl= sc.nextLine().trim();
                    System.out.println(dl.isEmpty()? sw.iniciarJuego(titulo,online)
                                                : sw.iniciarJuego(titulo,online, dl.split("\\s*,\\s*")));
                }
                else if(op==3){
                    System.out.print("SSID: "); String ssid=sc.nextLine();
                    System.out.print("¿Red abierta? (s/n): "); boolean abierta=leerSiNo(sc);
                    if(abierta) System.out.println(sw.conectarRed(ssid));
                    else{
                        System.out.print("Contraseña: "); String pwd=sc.nextLine();
                        System.out.print("¿Recordar credenciales? (s/n): "); boolean recordar=leerSiNo(sc);
                        System.out.println(sw.conectarRed(ssid,pwd,recordar));
                    }
                }
                else if(op==4){
                    System.out.print("¿Forzar actualización? (s/n): "); boolean forzar=leerSiNo(sc);
                    if(forzar) sw.actualizarSoftware(true);
                    System.out.print("Canal (estable/beta/preview o vacío): ");
                    String canal=sc.nextLine();
                    if(!canal.isBlank()) sw.actualizarSoftware(canal);
                    if(!forzar && canal.isBlank()) sw.actualizarSoftware();
                }
                else if(op==5){
                    System.out.print("¿Perfil (alto/equilibrado/ahorro) o vacío?: ");
                    String perfil=sc.nextLine();
                    if(!perfil.isBlank()) System.out.println(sw.getDuracionBateria(perfil));
                    else{
                        System.out.print("Brillo (0..100): "); int brillo=leerEnteroSeguro(sc);
                        System.out.print("WiFi ON? (s/n): "); boolean wifi=leerSiNo(sc);
                        System.out.print("Bluetooth ON? (s/n): "); boolean bt=leerSiNo(sc);
                        System.out.print("¿Dock? (s/n): "); boolean dock=leerSiNo(sc);
                        System.out.println(sw.getDuracionBateria(brillo,wifi,bt,dock));
                    }
                }
                else if(op==6){
                    if(sw instanceof Estandar){
                        System.out.println("1) Poner en Modo TV");
                        System.out.println("2) Desmontar Joy-Con");
                        System.out.print("Elige [1-2]: ");
                        int s=leerEnteroSeguro(sc);
                        if(s==1) ((Estandar)sw).ponerEnModoTV();
                        else if(s==2) ((Estandar)sw).desmontarJoyCon();
                    } else if(sw instanceof Lite){
                        System.out.println("1) Calibrar botones integrados");
                        System.out.println("2) Activar BT para audífonos");
                        System.out.print("Elige [1-2]: ");
                        int s=leerEnteroSeguro(sc);
                        if(s==1) ((Lite)sw).calibrarBotonesIntegrados();
                        else if(s==2) ((Lite)sw).activarBluetoothParaAudifonos();
                    } else if(sw instanceof OledZelda){
                        ((OledZelda)sw).mostrarEdicionZelda();
                    } else if(sw instanceof OledEdicionEspecial){
                        ((OledEdicionEspecial)sw).mostrarTematica();
                    } else if(sw instanceof Oled){
                        System.out.println("1) Activar modo colores vivos");
                        System.out.println("2) Usar soporte ajustable");
                        System.out.print("Elige [1-2]: ");
                        int s=leerEnteroSeguro(sc);
                        if(s==1) ((Oled)sw).activarModoColoresVivos();
                        else if(s==2) ((Oled)sw).usarSoporteAjustable();
                    } else {
                        System.out.println("Sin acciones especiales para este modelo.");
                    }
                }
                else if(op==0){
                    System.out.println("¡Hasta luego!");
                }
            } while(op!=0);
        } finally {
            sc.close();
        }
    }

    // Helpers
    private static int leerEnteroSeguro(Scanner sc){
        while(true){
            String line=sc.nextLine().trim();
            try{ return Integer.parseInt(line); }
            catch(NumberFormatException e){ System.out.print("Número inválido. Intenta de nuevo: "); }
        }
    }
    private static boolean leerSiNo(Scanner sc){
        while(true){
            String s=sc.nextLine().trim().toLowerCase();
            if(s.equals("s")||s.equals("si")||s.equals("sí")) return true;
            if(s.equals("n")||s.equals("no")) return false;
            System.out.print("Responde s/n: ");
        }
    }
}

// ================== SUBCLASES ==================
class Estandar extends NintendoSwitchApp {
    private boolean controlesRemovibles = true;
    private String soporteTrasero = "simple";
    public Estandar(){
        super("NVIDIA Custom Tegra","NVIDIA GM20B Maxwell",4,32,"WiFi, Bluetooth","LCD",6.2f,"1280x720");
        this.modelo="Nintendo Switch ESTÁNDAR";
    }
    @Override public void ponerEnModoTV(){ System.out.println("Modo TV activado (dock)."); }
    @Override public void desmontarJoyCon(){
        if(controlesRemovibles) System.out.println("Joy-Con desmontados.");
        else noDisponible("Desmontar Joy-Con");
    }
}

class Lite extends NintendoSwitchApp {
    private boolean vibracionHD=false;
    public Lite(){
        super("NVIDIA Custom Tegra","NVIDIA GM20B Maxwell",4,32,"WiFi, Bluetooth","LCD",5.5f,"1280x720");
        this.modelo="Nintendo Switch LITE";
    }
    @Override public void ponerEnModoTV(){ noDisponible("Modo TV / Dock"); }
    @Override public void desmontarJoyCon(){ noDisponible("Desmontar Joy-Con (controles integrados)"); }
    @Override public void calibrarBotonesIntegrados(){ System.out.println("Botones integrados calibrados."); }
    @Override public void activarBluetoothParaAudifonos(){ System.out.println("Bluetooth activado para audífonos."); }
}

class Oled extends NintendoSwitchApp {
    private String soporteTrasero="ajustable";
    private boolean puertoEthernet=true;
    public Oled(){
        super("NVIDIA Custom Tegra","NVIDIA GM20B Maxwell",4,64,"WiFi, Bluetooth","OLED",7.0f,"1280x720");
        this.modelo="Nintendo Switch OLED";
    }
    @Override public void activarModoColoresVivos(){
        if(!"OLED".equalsIgnoreCase(pantallaTipo)){ noDisponible("Colores vivos (requiere OLED)"); return; }
        System.out.println("Modo de colores vivos activado.");
    }
    @Override public void usarSoporteAjustable(){ System.out.println("Usando soporte trasero ajustable."); }
    @Override public void ponerEnModoTV(){ System.out.println("Modo TV activado (dock con Ethernet="+(puertoEthernet?"sí":"no")+")."); }
    @Override public void desmontarJoyCon(){ System.out.println("Joy-Con desmontados."); }
}

class OledEdicionEspecial extends Oled {
    private String tematica, colorEdicion; private boolean incluyeFunda;
    public OledEdicionEspecial(String tem,String color,boolean funda){
        super(); this.tematica=tem; this.colorEdicion=color; this.incluyeFunda=funda;
        this.modelo="Nintendo Switch OLED - Edición Especial ("+tematica+")";
    }
    @Override public void mostrarTematica(){
        System.out.println("Edición Especial -> temática: "+tematica+
                ", color: "+colorEdicion+", incluye funda: "+(incluyeFunda?"sí":"no"));
    }
}

class OledZelda extends Oled {
    private boolean incluyeJuegoZelda; private String arteJoyCon, versionJuego;
    public OledZelda(boolean inc,String arte,String ver){
        super(); incluyeJuegoZelda=inc; arteJoyCon=arte; versionJuego=ver;
        this.modelo="Nintendo Switch OLED - Edición Zelda";
    }
    @Override public void mostrarEdicionZelda(){
        System.out.println("Edición Zelda:");
        System.out.println("- Arte Joy-Con: "+(arteJoyCon==null? "N/D": arteJoyCon));
        System.out.println("- "+(incluyeJuegoZelda? "Incluye juego: "+versionJuego : "No incluye juego"));
    }
}
