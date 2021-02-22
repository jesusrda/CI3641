package src;

import java.util.TreeSet;
import java.util.TreeMap;
import java.util.ArrayList;

public class BuddyAllocManager {

    private int size;                               // memory cap
    private TreeMap<String, Block> nameToBlock;     // reserved blocks
    private ArrayList<TreeSet<Block>> freeBlocks;   // free blocks

    //
    // Static function to get the order of a number. Order is defined as
    // ceiling(log2(n))
    //
    private static int order(int size) {

        int ord = 0;
        int x = 1;
        while (size > x) {
            x <<= 1;
            ord++;
        }
        return ord;
    }

    //
    // Class constructor
    //
    public BuddyAllocManager(int size) {
       
        this.size = size;
        nameToBlock = new TreeMap<>();

        int sz = order(size) + 1;
        freeBlocks = new ArrayList<>(sz);
        for (int i = 0; i < sz; i++) {
            freeBlocks.add(new TreeSet<>()) ;
        }

        freeBlocks.get(sz - 1).add(new Block(0,size));       
    }

    //
    // Allocation function
    //
    public void alloc(String name, int size) throws  OperationFailedException {

        if (!nameToBlock.isEmpty() && nameToBlock.containsKey(name)) {
            throw new OperationFailedException("El nombre ya tiene un bloque"
                                             + " de memoria asociado.");
        }
        
        int ord = order(size);
        int maxOrd = order(this.size);
        boolean found = false;
        while (ord <= maxOrd) {
            found = !freeBlocks.get(ord).isEmpty();
            if (found) 
                break;            
            ord++;
        }
        
        if (!found) {
            throw new OperationFailedException("No existe un bloque contiguo" 
                                             + " de memoria lo suficientemente"
                                             + " grande para satisfacer la"
                                             + " operación");
        }

        Block block = freeBlocks.get(ord).first();
        freeBlocks.get(ord).remove(block);
        alloc(block.first, block.size, name, size);
    }

    //
    // Allocation recursion to find the first block that fit the space
    // that we want to reserve
    //
    public void alloc(int blockFirst, int blockSize, String name, int size) {
        
        if (blockSize/2 >= size) {
            int nextSize = blockSize/2;
            int ord = order(nextSize);
            freeBlocks.get(ord).add(new Block(blockFirst+nextSize, nextSize));
            alloc(blockFirst, nextSize, name, size);
        } else {
            nameToBlock.put(name, new Block(blockFirst, blockSize, name));
        }

    }

    //
    // Free function
    //
    public void free(String name) throws OperationFailedException {

        if (nameToBlock.isEmpty() || !nameToBlock.containsKey(name)) {
            throw new OperationFailedException("El nombre no tiene un bloque"
                                             + " de memoria asociado.");
        }

        Block block = nameToBlock.get(name);
        nameToBlock.remove(name);
        free(0,size,block);
    }

    //
    // Free recursion to rebuild the buddy blocks if needed
    //
    public void free(int first, int size, Block block) {

        int ord = order(size);
        if (first == block.first && block.size == size) {
            block.name = "";
            freeBlocks.get(ord).add(block);     
        } else if (first <= block.first 
                && block.first + block.size <= first + size) {
            int nextSize = size/2;
            free(first, nextSize, block);
            free(first+nextSize, nextSize, block);
            Block left = new Block(first, nextSize);
            Block right = new Block(first+nextSize, nextSize);
            if (freeBlocks.get(ord-1).contains(left) &&
                freeBlocks.get(ord-1).contains(right)) {
                    freeBlocks.get(ord-1).remove(left);
                    freeBlocks.get(ord-1).remove(right);
                    freeBlocks.get(ord).add(new Block(first, size));
                }
        }
    }

    //
    // Function to print memory state
    //
    public void print() {
        
        TreeSet<Block> tree = new TreeSet<>();
        int sz = order(size) + 1;
        
        for(int i = 0; i < sz; i++) {
            tree.addAll(freeBlocks.get(i));
        }
        
        tree.addAll(nameToBlock.values());

        System.out.println("Estado de la memoria:");
        for(Block block : tree) {
            System.out.println("Inicio: " + block.first 
                             + " Tamaño: " + block.size
                             + " Contenido: " + (block.name.equals("") ? 
                                                    "Vacío" : block.name));
        }
    }
}