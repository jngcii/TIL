import java.util.*;
import java.io.*;
class Edge {
    int to;
    int cost;
    Edge(int to, int cost) {
        this.to = to;
        this.cost = cost;
    }
}
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bf.readLine());
        ArrayList<Edge>[] a = new ArrayList[n+1];
        for (int i=1; i<=n; i++) {
            a[i] = new ArrayList<>();
        }
        for (int i=0; i<n-1; i++) {
            String[] line = bf.readLine().split(" ");
            int x = Integer.parseInt(line[0]);
            int y = Integer.parseInt(line[1]);
            int z = Integer.parseInt(line[2]);
            a[x].add(new Edge(y,z));
            a[y].add(new Edge(x,z));
        }
        int[] depth = new int[n+1];
        boolean[] check = new boolean[n+1];
        int[] parent = new int[n+1];
        int[] dist = new int[n+1];
        Queue<Integer> q = new LinkedList<Integer>();
        check[1] = true;
        depth[1] = 0;
        parent[1] = 0;
        dist[1] = 0;
        q.add(1);
        while (!q.isEmpty()) {
            int x = q.remove();
            for (Edge e : a[x]) {
                int y = e.to; 
                if (check[y] == false) {
                    dist[y] = dist[x] + e.cost;
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
            int ans = dist[x] + dist[y];
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
            ans -= 2*dist[x];
            bw.write(ans + "\n");
        }
        bw.flush();
    }
}