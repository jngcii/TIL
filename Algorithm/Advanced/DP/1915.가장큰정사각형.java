import java.util.*;
public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[][] a = new int[n+1][m+1];
        int[][] d = new int[n+1][m+1];
        for (int i=1; i<=n; i++) {
            String s = sc.next();
            for (int j=1; j<=m; j++) {
                a[i][j] = s.charAt(j-1)-'0';
            }
        }
        int ans = 0;
        for (int i=1; i<=n; i++) {
            for (int j=1; j<=m; j++) {
                if (a[i][j] == 0) {
                    continue;
                }
                d[i][j] = Math.min(Math.min(d[i-1][j-1], d[i-1][j]), d[i][j-1]) + 1;
                if (ans < d[i][j]) {
                    ans = d[i][j];
                }
            }
        }
        System.out.println(ans*ans);
    }
}