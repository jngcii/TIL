import java.util.*;
public class Main {
    static final long mod = 1000003;
    static long[][] multiplication(long[][] a, long[][] b) {
        int n = a.length;
        long[][] c = new long[n][n];
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                c[i][j] = 0;
                for (int k=0; k<n; k++) {
                    c[i][j] += a[i][k] * b[k][j];
                }
                c[i][j] %= mod;
            }
        }
        return c;
    }
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int s = sc.nextInt();
        int e = sc.nextInt();
        int t = sc.nextInt();
        long[][] ans = new long[n*5][n*5];
        for (int i=0; i<n*5; i++) {
            ans[i][i] = 1;
        }
        long[][] a = new long[n*5][n*5];
        for (int i=0; i<n; i++) {
            for (int j=0; j<4; j++) {
                a[5*i+j][5*i+j+1] = 1;
            }
        }
        for (int i=0; i<n; i++) {
            String line = sc.next();
            for (int j=0; j<n; j++) {
                int v = line.charAt(j)-'0';
                if (v > 0) {
                    a[5*i+v-1][5*j] = 1;
                }
            }
        }
        while (t > 0) {
            if (t % 2 == 1) {
                ans = multiplication(ans, a);
            }
            a = multiplication(a, a);
            t >>= 1;
        }
        s -= 1;
        e -= 1;
        System.out.println(ans[5*s][5*e]);
    }
}