import { Entity, Column, PrimaryGeneratedColumn } from 'typeorm';

@Entity()
export class Node {
  @PrimaryGeneratedColumn()
  id: number;

  @Column()
  nodeId: string;

  @Column()
  nodeName: string;

  @Column()
  nodeType: string;

  @Column()
  nodeStatus: string;

  @Column()
  nodeVersion: string;

  @Column()
  nodePublicKey: string;

  @Column()
  nodePrivateKey: string;
}
