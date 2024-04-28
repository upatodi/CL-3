import java.sql.*;
import java.rmi.*;
import java.io.*;
import java.util.*;
import java.util.Vector.*;
import java.lang.*;
import java.rmi.registry.*;

public class Client
{ 
    static String send_details;
    public static void main(String args[])
    {
        Client c = new Client();
        BufferedReader b = new BufferedReader(new InputStreamReader(System.in));
        int ch;
        String name, date, type_of_room, breakfast;
        try 
        { 
            Registry r1 = LocateRegistry.getRegistry ( "localhost", 1030);
            DBInterface DI=(DBInterface)r1.lookup("DBServ");
            do
            {
                System.out.println("1. Book Room for Specific Guest\n2. Cancel the Booking for the Guest \nEnter ur choice");
                ch = Integer.parseInt(b.readLine());
                switch(ch)
                {
                    case 1:
                    {
                        System.out.println(" \nEnter the name of the guest:");
                        name = b.readLine();
                        System.out.println(" \nEnter Check-In Date(YYYY-MM-DD):");
                        date = b.readLine();
                        System.out.println(" \nEnter which type of room you prefer(Standard / Deluxe):");
                        type_of_room = b.readLine();
                        System.out.println(" \nDo you want to include Breakfast(Yes / No):");
                        breakfast = b.readLine();
                        send_details = DI.input(name, date, "Book");
                        System.out.println(" \n"+send_details+"\n");
                        break;
                    }
                    case 2:
                    {
                        System.out.println(" \nEnter the name of the guest:");
                        name = b.readLine();
                        System.out.println(" \nEnter Check-In Date(YYYY-MM-DD):");
                        date = b.readLine();
                        send_details = DI.input(name, date, "Cancel");
                        System.out.println(" \n"+send_details+"\n");
                        break;
                    }
                }
            }while(ch>0);
        }       
        catch (Exception e)
        {
            System.out.println("ERROR: " +e.getMessage());
        }
    }
}