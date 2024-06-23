// node-management.component.ts
import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

interface Node {
  id: number;
  name: string;
  ipAddress: string;
  status: string;
}

@Component({
  selector: 'app-node-management',
  template: `
    <div>
      <h1>Node Management</h1>
      <form(ngSubmit)="createNode()">
        <label>
          Name:
          <input type="text" [(ngModel)]="newNode.name">
        </label>
        <label>
          IP Address:
          <input type="text" [(ngModel)]="newNode.ipAddress">
        </label>
        <label>
          Status:
          <input type="text" [(ngModel)]="newNode.status">
        </label>
        <button type="submit">Create Node</button>
      </form>
      <ul>
        <li *ngFor="let node of nodes">
          {{ node.name }} ({{ node.ipAddress }}) - {{ node.status }}
        </li>
      </ul>
    </div>
  `,
  styles: [`
    :host {
      display: block;
      padding: 20px;
    }
  `]
})
export class NodeManagementComponent implements OnInit {
  nodes: Node[] = [];
  newNode: Node = { name: '', ipAddress: '', status: '' };

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
    this.http.get('https://example.com/nodes')
      .subscribe(response => {
        this.nodes = response as Node[];
      });
  }

  createNode(): void {
    this.http.post('https://example.com/nodes', this.newNode)
      .subscribe(response => {
        this.nodes.push(response as Node);
        this.newNode = { name: '', ipAddress: '', status: '' };
      });
  }
}
