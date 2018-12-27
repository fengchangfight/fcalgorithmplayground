public class IsPowerof2Demo {

    public static boolean isPoweroftwo(int x){
        if(x<1){
            return false;
        }

        int andVal = x&(x-1);
        int xorVal = x^(x-1);

        if(andVal==0 && xorVal==2*x-1){
            return true;
        }

        return false;
    }

    public static void main(String[] args) {
        for(int i=0;i<100;i++){
            if(isPoweroftwo(i)){
                System.out.println(i);
            }
        }
    }
}
