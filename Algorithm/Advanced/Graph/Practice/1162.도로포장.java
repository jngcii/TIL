import java.util.*;
class Node implements Comparable<Node> {
    long cost;
    int vertex;
    int step;
    Node(long cost, int vertex, int step) {
        this.cost = cost;
        this.vertex = vertex;
        this.step = step;
    }
    public int compareTo(Node that) {
        if (this.cost < that.cost) {
            return -1;
        } else if (this.cost == that.cost) {
            return 0;
        } else {
            return 1;
        }
    }
}
class Edge{
    int to, cost;
    Edge(int to, int cost) {
        this.to = to;
        this.cost = cost;
    }
}
public class Main {
    static final long inf = 1000000000L*50000L;
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int k = sc.nextInt();
            List<Edge>[] a = (List<Edge>[]) new List[n+1];
        for (int i=1; i<=n; i++) {
            a[i] = new ArrayList<Edge>();
        }
        for (int i=0; i<m; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            int z = sc.nextInt();
            a[x].add(new Edge(y, z));
            a[y].add(new Edge(x, z));
        }
        long[][] dist = new long[n+1][k+1];
        boolean[][] check = new boolean[n+1][k+1];
        for (int i=1; i<=n; i++) {
            for (int j=0; j<=k; j++) {
                dist[i][j] = inf;
            }
        }
        dist[1][0] = 0;
        PriorityQueue<Node> q = new PriorityQueue<>();
        q.add(new Node(0, 1, 0));
        while (!q.isEmpty()) {
            Node temp = q.remove();
            int x = temp.vertex;
            int step = temp.step;
            if (check[x][step]) continue;
            check[x][step] = true;
            for (Edge e : a[x]) {
                int y = e.to;
                if (step+1 <= k && dist[y][step+1] > dist[x][step]) {
                    dist[y][step+1] = dist[x][step];
                    q.add(new Node(dist[y][step+1], y, step+1));
                }
                if (dist[y][step] > dist[x][step] + e.cost) {
                    dist[y][step] = dist[x][step] + e.cost;
                    q.add(new Node(dist[y][step], y, step));
                }
            }
        }
        long ans = inf;
        for (int i=1; i<=k; i++) {
            if (check[n][i] && ans > dist[n][i]) {
                ans = dist[n][i];
            }
        }
        System.out.println(ans);
    }
}