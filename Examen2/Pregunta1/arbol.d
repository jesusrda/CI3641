class Arbol(T) {

    // Si es necesario, se deben sobrecargar los operadores opEquals y opCmp 
    // en T (para ser capaz de usar <=, >=, ==)

    private Arbol izq; // Nodo Izquierdo
    private Arbol der; // Nodo Dererecho
    private T val;     // Valor del nodo

    // Constructor
    this(T val) {
        this.val = val;
        izq = der = null;
    }

    public bool esDeBusqueda () {

        if (izq is null && der is null) {
            return true;
        } else if (izq is null) {
            return der.esDeBusqueda() && val <= der.val;
        } else if (der is null) {
            return izq.esDeBusqueda() && val >= izq.val;
        } else {
            return izq.esDeBusqueda() 
                && der.esDeBusqueda()
                && val >= izq.val
                && val <= der.val;
        }
    }
}