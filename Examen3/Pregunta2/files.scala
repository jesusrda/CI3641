import scala.io.StdIn.readLine
import scala.concurrent.{Await, Future}
import scala.concurrent.duration._
import scala.util.{Success, Failure}
import scala.concurrent.ExecutionContext.Implicits.global
import java.io.File

object FileCounter {

    // Función para contar los archivos en un subdirectorio
    def countPathRecursive(dir: File): Future[Int] = Future {

        // Listamos los subdirectorios
        val dirs = dir.listFiles.filter(f => f.isDirectory)
        // Creamos una secuencia de Futures, donde cada uno explora un nuevo subdirectorio
        val sequence = dirs.map(f => countPathRecursive(f)).toSeq
        // Contamos los archivos en el subdirectorio actual
        var count = dir.listFiles.count(f => f.isFile)
        if (sequence.length > 0) {
            // Esperamos por el resultado de la secuencia de futures. Esto es, esperamos
            // a que cada hilo tenga una respuesta
            var x = Await.result(Future.sequence(sequence), Duration.Inf).sum
            // Aumentamos el resultado con la respuesta de los hilos
            count += x
        }
        count
    }

    def countPath(path: String): Int = {

        val dir = new File(path)
        // Contamos los archivos recursivamente en cada subdirectorio
        var futureCount = countPathRecursive(dir)
        var count = Await.result(futureCount, Duration.Inf)
        count
    }

    // Main para probar el programa
    def main(args: Array[String]): Unit = {

        val path = readLine()
        println(countPath(path))
    }
}
