public class Programme{
    public static void main(String[] args) {
        System.out.println("Hello World !");
        try{
            System.out.println(10/0);
        }catch(ArithmeticException ex){
           ex.printStackTrace();
        }catch(Exception exception){
            System.out.println(exception.getStackTrace());
        }
        finally{
            System.out.println("Execution completed");
        }
        System.out.println("Hello Narasimha");
    }
}