import java.util.*;
public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] d = new int[n][n];
        boolean[][] unused = new boolean[n][n];
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                d[i][j] = sc.nextInt();
            }
        }
        for (int k=0; k<n; k++) {
            for (int i=0; i<n; i++) {
                if (i == k) continue;
                for (int j=0; j<n; j++) {
                    if (i == j) continue;
                    if (k == j) continue;
                    if (d[i][j] > d[i][k] + d[k][j]) {
                        System.out.println(-1);
                        System.exit(0);
                    }
                    if (d[i][j] == d[i][k] + d[k][j]) {
                        unused[i][j] = true;
                    }
                }
            }
        }
        int ans = 0;
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                if (unused[i][j] == false) {
                    ans += d[i][j];
                }
            }
        }
        ans /= 2;
        System.out.println(ans);
    }
}