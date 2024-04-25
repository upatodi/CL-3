import java.io.*;
import java.rmi.*;
import java.rmi.registry.*;

public class Client {
    public static void main(String args[]) {
        try {
            Registry registry = LocateRegistry.getRegistry("localhost", 1030);
            DBInterface dbInterface = (DBInterface) registry.lookup("DBServ");
            BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

            System.out.println("Enter the first string:");
            String name1 = reader.readLine();

            System.out.println("Enter the second string:");
            String name2 = reader.readLine();

            String concatenatedString = dbInterface.input(name1, name2);
            System.out.println("Concatenated String is: " + concatenatedString);
        } catch (Exception e) {
            System.out.println("ERROR: " + e.getMessage());
        }
    }
}
