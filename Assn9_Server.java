import java.util.*;
import java.sql.*;
import java.rmi.*;
import java.rmi.server.*;
import java.util.Vector;
interface DBInterface extends Remote
{
    public String input(String name, String date, String operation) throws RemoteException;
}

public class Server extends UnicastRemoteObject implements DBInterface
{
    Map<String, String[]> dateMap = new HashMap<>();
    public Server() throws RemoteException
    { 
        try
        {
            System.out.println("Initializing Server\nServer Ready");
        }
        catch (Exception e)
        {
            System.out.println("ERROR: " +e.getMessage());
        }
    }

    public static void main(String[] args)
    { 
        try
        { 
            Server rs=new Server();
            java.rmi.registry.LocateRegistry.createRegistry(1030).rebind("DBServ", rs);
        }
        catch (Exception e)
        {
            System.out.println("ERROR: " +e.getMessage());
        }
    }

    public String input(String name, String date, String operation)
    {
        try
        {
            if(operation.equals("Book"))
            {
                if(dateMap.containsKey(date))
                {
                    String[] str = dateMap.get(date);
                    int nextEmptyIndex = -1;
                    for (int i = 0; i < str.length; i++) 
                    {
                        if (str[i].equals(null)) 
                        {
                            nextEmptyIndex = i;
                            break;
                        }
                    }
                    if(nextEmptyIndex == -1) 
                    {
                        return "Hotel is full for Date "+date;
                    }
                    else
                    {
                        str[nextEmptyIndex] = name;
                        // dateMap.get(date) = str;
                        return "\nBooking for "+name+" for Date "+date+" has been confirmed.";
                    }
                }
                else
                {
                    System.out.println("In book section else");
                    String[] strings = {name, "", "", "", "", "", "", "", "", ""};
                    dateMap.put(date, strings);
                    return "\nBooking for "+name+" for Date "+date+" has been confirmed.";
                }
            }
            else if(operation.equals("Cancel"))
            {
                if (dateMap.containsKey(date)) 
                {
                    String[] str = dateMap.get(date);
        
                    int index = -1;
                    for (int i = 0; i < str.length; i++) 
                    {
                        if (str[i].equals(name)) 
                        {
                            index = i;
                            break;
                        }
                    }
        
                    if (index == -1) 
                    {
                        return "No bookings available with this name.";
                        
                    } else 
                    {
                        str[index] = "";
                        // dateMap.get(date) = str;
                        return "\nCancellation for "+name+" for Date "+date+" on "+date+" is successful.";
                    }
                } 
                else 
                {
                    return "No bookings available on this date.";
                }
            }
        }
        catch (Exception e)
        {
            return "ERROR: " +e.getMessage(); 
        }
        return "";
    }
}
