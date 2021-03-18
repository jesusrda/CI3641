import std.stdio : writeln;

// Clase para representar numeros de Church
class Church {

    // Predecesor del número actual
    private Church pred;

    // Sobrecarga de la suma
    Church opAdd(Church rhs) {
        
        // Inicializamos en cero
        Church ret = new Zero();
    
        Church cur = this;

        while (cur.pred !is null){
            ret = new Suc(ret);
            cur = cur.pred;
        }

        cur = rhs;
        
        while (cur.pred !is null) {
            ret = new Suc(ret);
            cur = cur.pred;
        }

        return ret;                
    }

    // Sobrecarga de la multiplicación
    Church opMul(Church rhs) {
        
        Church ret = new Zero();
    
        Church it = this;
        
        while (it.pred !is null) {
            
            Church it2 = rhs;
            while (it2.pred !is null) {
                ret = new Suc(ret);
                it2 = it2.pred;
            }
            
            it = it.pred;
        }

        return ret;                
    }
}

// Clase para representar al Cero en los numeros de church. Hereda de Church
class Zero : Church
{
   this()
   {
       this.pred = null; // No tiene predecesor
   }
}

// Clase para representar a un sucesor. Hereda de church
class Suc : Church
{  
    this (Church pred)
    {
        this.pred = pred;
    }
}

// Pequeña función para pasar una instancia de Church a un entero
int churchToInt(Church c) 
{
    int ret = 0;
    while (!(c.pred is null))
    {
        c = c.pred;
        ret++;
    }
    return ret;
}


// Pequeña función para probar los resultados
// Para compilar, podemos hacer uso de gdc, el compilador para el lenguaje d de
// la familia de compiladores de gcc. Es suficiente con ejecutar:
// > gdc -o church church.d
int main()
{

    Church zero = new Zero();
    Church uno = new Suc(zero);
    Church dos = new Suc(uno);
    Church tres = new Suc(dos);
    writeln(churchToInt(dos*tres));
    writeln(churchToInt(dos+uno));
    writeln(churchToInt(tres*zero));
    writeln(churchToInt(zero+uno));
    return 0;
}