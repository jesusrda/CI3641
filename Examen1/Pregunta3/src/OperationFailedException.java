package src;

//
// Class to represent an error found when executing queries
//
public class OperationFailedException extends Exception {

    private static final long serialVersionUID = 1L;

    public OperationFailedException(String message) {
        super(message);
    }
}