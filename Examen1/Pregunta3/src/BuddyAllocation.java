package src;

import java.util.Scanner;


//
// Class for main loop, taking input and calling operations
//
 class BuddyAllocation {

    public void run(int n) {

        BuddyAllocManager manager = new BuddyAllocManager(n);
        boolean done = false;
        Scanner scanner = new Scanner(System.in);
        while (!done) {
            String option = scanner.next();
            String name;
            switch (option) {
                case "RESERVAR":
                    name = scanner.next();
                    int size = Integer.parseInt(scanner.next());
                    try {
                        manager.alloc(name, size);
                    } catch (OperationFailedException e) {
                        System.out.println("Error: ");
                        System.out.println(e.getMessage());
                    }
                    break;
                case "LIBERAR":
                    name = scanner.next();
                    try {
                        manager.free(name);
                    } catch (OperationFailedException e) {
                        System.out.println("Error: ");
                        System.out.println(e.getMessage());
                    }
                    break;
                case "MOSTRAR":
                    manager.print();
                    break;
                case "SALIR":
                    done = true;
                    break; 
                default:
                    System.out.println("Opción incorrecta.");        
                    break;           
            }
        }
        scanner.close();
    }

    public static int lastPow2(int n) {
        int pow = 1;
        while(pow <= n) {
            pow <<= 1;
        }
        return pow >> 1;
    }

    //
    // Main
    //
    public static void main(String[] args){

        if(args.length < 1) {
            System.out.println("Debe especificar el tamaño de la memoria.");
            return;
        }

        int n = Integer.parseInt(args[0]);
        int pow = lastPow2(n);
    
        if (pow != n) { 
            System.out.println(n + " no es potencia de dos.");
            System.out.println("Se usará la mayor potencia de dos posible: " + pow);
        }

        BuddyAllocation test = new BuddyAllocation();
        test.run(pow);        
    } 
}