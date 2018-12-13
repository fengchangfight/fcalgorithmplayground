public class Sqrt2 {
    public static double sqrt2(int iter_cnt){
        int a =1, b=1;

        for(int i=0;i<iter_cnt;i++){
            int olda = a;
            a = olda+b;
            b = 2*olda+b;
            System.out.printf("After %d iteration, a is: %d, b is %d", i, a, b);
            System.out.println("");
        }
        double result = b*1.0/a;
        return result;
    }

    public static void main(String[] args) {
        int iter_cnt = 20;
        double result = sqrt2(iter_cnt);
        System.out.println(result);
    }
}
