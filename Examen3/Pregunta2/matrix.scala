import scala.io.StdIn.readLine
import scala.concurrent.{Await, Future}
import scala.concurrent.duration._
import scala.concurrent.ExecutionContext.Implicits.global

object Matrix {
    
    // Función para sumar los elementos de dos arreglos y envolverlos en un Future
    def sumRow(row1: Array[Int], 
               row2: Array[Int]): Future[Array[Int]] = Future {
        (row1 zip row2).map{case(x, y) => x + y}
    }

    def sumMatrix(a1: Array[Array[Int]], 
                       a2: Array[Array[Int]]): Array[Array[Int]] = {

        // Para cada una de las filas, creamos un Future que calculará el
        // resultado de sumarlas
        val futures: Seq[Future[Array[Int]]] = (a1 zip a2).map {
            case(x, y) => sumRow(x,y)
        }.toSeq

        // Juntamos todos los futures en una secuencia
        val sequence = Future.sequence(futures)
        // Esperamos por el resultado de todas las sumas y retornamos
        var result = Await.result(sequence, Duration.Inf)
        result.toArray
    } 
    
    // Main para probar el programa
    def main(args: Array[String]): Unit = {

        val Array(rows, cols) = readLine().split(" ").map(_.toInt)

        var a1 = Array.ofDim[Int](rows, cols)
        var a2 = Array.ofDim[Int](rows, cols)
        
        for (i <- 0 until rows) { 
            a1(i) = readLine().split(" ").map(_.toInt)
        }

        for (i <- 0 until rows) { 
            a2(i) = readLine().split(" ").map(_.toInt)
        }

        var result = sumMatrix(a1,a2)
        for (i <- 0 until rows) {
            for (j <- 0 until cols) {
                print(result(i)(j))
                print(" ")
            }
            println()
        }
    }
}
