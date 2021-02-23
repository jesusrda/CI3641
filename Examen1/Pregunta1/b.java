class Ejercicio1b {

    // Factorial
    public static int Fact(int n) {
        
        if (n == 0) 
            return 1;

        return n*Fact(n-1);
    }

    // Producto de Matrices
    public static int[][] Prod(int[][] A,
                               int[][] B,
                               int N,
                               int M,
                               int P){
        
        int[][] C = new int[N][P];

        for(int i = 0; i < N; i++){
            for(int j = 0; j < P; j++){ 
                C[i][j] = 0;
                for(int k=0; k < M; k++){
                    C[i][j] += A[i][k] * B[k][j];
                }
            }
        }

        return C;                       
    }
}