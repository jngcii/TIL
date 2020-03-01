import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bf.readLine());
        ArrayList<Integer>[] a = new ArrayList[n+1];
        for (int i=1; i<=n; i++) {
            a[i] = new ArrayList<>();
        }
        for (int i=1; i<=n-1; i++) {
            String[] line = bf.readLine().split(" ");
            int x = Integer.parseInt(line[0]);
            int y = Integer.parseInt(line[1]);
            a[x].add(y);
            a[y].add(x);
        }
        int[] depth = new int[n+1];
        boolean[] check = new boolean[n+1];
        int[] parent = new int[n+1];
        int start = 1;
        Queue<Integer> q = new LinkedList<Integer>();
        check[start] = true;
        depth[start] = 0;
        parent[start] = 0;
        q.add(start);
        while (!q.isEmpty()) {
            int x = q.remove();
            for (int y : a[x]) {
                if (check[y] == false) {
                    depth[y] = depth[x] + 1;
                    check[y] = true;
                    parent[y] = x;
                    q.add(y);
                }
            }
        }
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int m = Integer.parseInt(bf.readLine());
        while (m-- > 0) {
            String[] line = bf.readLine().split(" ");
            int x = Integer.parseInt(line[0]);
            int y = Integer.parseInt(line[1]);
            if (depth[x] < depth[y]) {
                int temp = x;
                x = y;
                y = temp;
            }
            while (depth[x] != depth[y]) {
                x = parent[x];
            }
            while (x != y) {
                x = parent[x];
                y = parent[y];
            }
            bw.write(x + "\n");
        }
        bw.flush();
    }
}