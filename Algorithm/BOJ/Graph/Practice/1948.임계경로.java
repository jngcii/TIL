import java.util.*;

class Edge {
    int to, cost;
    Edge(int to, int cost) {
        this.to = to;
        this.cost = cost;
    }
}
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        List<Edge>[] a = (List<Edge>[]) new List[n+1];
        List<Edge>[] ar = (List<Edge>[]) new List[n+1];
        for (int i=1; i<=n; i++) {
            a[i] = new ArrayList<Edge>();
            ar[i] = new ArrayList<Edge>();
        }
        for (int i=0; i<m; i++) {
            int from = sc.nextInt();
            int to = sc.nextInt();
            int cost = sc.nextInt();
            a[from].add(new Edge(to, cost));
            ar[to].add(new Edge(from, cost));
        }
        int start = sc.nextInt();
        int end = sc.nextInt();
        Queue<Integer> q = new LinkedList<Integer>();
        int[] indegree = new int[n+1];
        int[] dist = new int[n+1];
        for (int i=1; i<=n; i++) {
            for (Edge e : a[i]) {
                indegree[e.to] += 1;
            }
        }
        q.add(start);
        while (!q.isEmpty()) {
            int from = q.remove();
            for (Edge e : a[from]) {
                int to = e.to;
                int cost = e.cost;
                if (dist[to] < dist[from] + cost) {
                    dist[to] = dist[from] + cost;
                }
                indegree[to] -= 1;
                if (indegree[to] == 0) {
                    q.add(to);
                }
            }
        }
        System.out.println(dist[end]);
        for (int i=1; i<=n; i++) {
            indegree[i] = 0;
        }
        for (int i=1; i<=n; i++) {
            for (Edge e : ar[i]) {
                indegree[e.to] += 1;
            }
        }
        boolean[] check = new boolean[n+1];
        q.add(end);
        check[end] = true;
        int ans = 0;
        while (!q.isEmpty()) {
            int from = q.remove();
            for (Edge e : ar[from]) {
                int to = e.to;
                int cost = e.cost;
                if (dist[from] - dist[to] == cost) {
                    if (check[from]) {
                        ans += 1;
                        check[to] = true;
                    }
                }
                indegree[to] -= 1;
                if (indegree[to] == 0) {
                    q.add(to);
                }
            }
        }
        System.out.println(ans);
    }
}