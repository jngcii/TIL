import java.util.*;
public class Main {
    static long[][] d = new long[31][31];
    static long calc(int f, int h) {
        if (d[f][h] != -1) return d[f][h];
        if (f == 0) return 1;
        if (h == 0) return d[f][h] = calc(f-1, h+1);
        return d[f][h] = calc(f-1,h+1) + calc(f,h-1);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        for (int i=0; i<31; i++) {
            Arrays.fill(d[i], -1);
        }
        while (true) {
            int n = sc.nextInt();
            if (n == 0) break;
            System.out.println(calc(n,0));
        }
    }
}