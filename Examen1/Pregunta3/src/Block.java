package src;

//
// Class used to represent a block of memory
//
class Block implements Comparable<Block> {

    public int first;    // start address of the block
    public int size;     // size of the block
    public String name;  // name of data in the block if reserved

    public Block(int first, int size) {
        this.first = first;
        this.size = size;
        this.name = "";
    }

    public Block(int first, int size, String name) {
        this.first = first;
        this.size = size;
        this.name = name;
    }

    public int compareTo(Block other) {
        return this.first == other.first ? this.size - other.size : 
                                           this.first - other.first;
    }
}