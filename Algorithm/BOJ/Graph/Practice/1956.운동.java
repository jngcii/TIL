import java.util.*;
public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[][] d = new int[n][n];
        while (m-- > 0) {
            int x = sc.nextInt();
            x -= 1;
            int y = sc.nextInt();
            y -= 1;
            int z = sc.nextInt();
            if (d[x][y] == 0) {
                d[x][y] = z;
            } else if (d[x][y] > z) {
                d[x][y] = z;
            }
        }
        for (int k=0; k<n; k++) {
            for (int i=0; i<n; i++) {
                for (int j=0; j<n; j++) {
                    if (d[i][k] != 0 && d[k][j] != 0) {
                        if (d[i][j] == 0 || d[i][j] > d[i][k] + d[k][j]) {
                            d[i][j] = d[i][k]+d[k][j];
                        }
                    }
                }
            }
        }
        int ans = -1;
        for (int i=0; i<n; i++) {
            if (d[i][i] != 0) {
                if (ans == -1 || ans > d[i][i]) {
                    ans = d[i][i];
                }
            }
        }
        System.out.println(ans);
    }
}