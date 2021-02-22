import src.*;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.BeforeEach;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

//
// Set of test cases
//
class TestAlloc {

    private int testSize = 32;
    private BuddyAllocManager manager; 
    private ByteArrayOutputStream stdoutContent;

    @BeforeEach
    public void prepare() {
        manager = new BuddyAllocManager(testSize); 
        stdoutContent = new ByteArrayOutputStream();
        System.setOut(new PrintStream(stdoutContent));
    }

    @Test
    public void testEmpty() throws OperationFailedException {
        manager.print();
        assertEquals("Estado de la memoria:\n"
                   + "Inicio: 0 Tamaño: 32 Contenido: Vacío\n", 
                     stdoutContent.toString());
    }

    @Test
    public void testAllocation() throws OperationFailedException {
        manager.alloc("Cero",4);
        manager.alloc("Uno",3);
        manager.alloc("Dos",1);
        manager.alloc("Tres",10);
        manager.alloc("Cuatro",4);
        manager.print();
        assertEquals("Estado de la memoria:\n"
                     + "Inicio: 0 Tamaño: 4 Contenido: Cero\n"
                     + "Inicio: 4 Tamaño: 4 Contenido: Uno\n"
                     + "Inicio: 8 Tamaño: 1 Contenido: Dos\n"
                     + "Inicio: 9 Tamaño: 1 Contenido: Vacío\n"
                     + "Inicio: 10 Tamaño: 2 Contenido: Vacío\n"
                     + "Inicio: 12 Tamaño: 4 Contenido: Cuatro\n"
                     + "Inicio: 16 Tamaño: 16 Contenido: Tres\n",
                        stdoutContent.toString());
    }

    @Test
    public void testFree() throws OperationFailedException {
        manager.alloc("Cero",4);
        manager.alloc("Uno",3);
        manager.alloc("Dos",1);
        manager.alloc("Tres",10);
        manager.alloc("Cuatro",4);
        manager.free("Cero");
        manager.free("Uno");
        manager.free("Dos");
        manager.print();
        assertEquals("Estado de la memoria:\n"
                     + "Inicio: 0 Tamaño: 8 Contenido: Vacío\n"
                     + "Inicio: 8 Tamaño: 4 Contenido: Vacío\n"
                     + "Inicio: 12 Tamaño: 4 Contenido: Cuatro\n"
                     + "Inicio: 16 Tamaño: 16 Contenido: Tres\n",
                        stdoutContent.toString());
    }

    @Test
    public void testNotEnoughSpace() throws OperationFailedException {
        manager.alloc("Cero",4);
        manager.alloc("Uno",3);
        manager.alloc("Dos",1);
        manager.alloc("Tres",10);
        manager.alloc("Cuatro",4);
        assertThrows(OperationFailedException.class, () -> manager.alloc("Cinco",8));
    }

    @Test
    public void testRepeatedName() throws OperationFailedException {
        manager.alloc("Cero",4);
        assertThrows(OperationFailedException.class, () -> manager.alloc("Cero",8));
    }

    @Test
    public void notInMemory() throws OperationFailedException {
        manager.alloc("Cero",4);
        assertThrows(OperationFailedException.class, () -> manager.free("Uno"));
    }   
}