import { Entity, Column, PrimaryGeneratedColumn } from 'typeorm';

@Entity()
export class Wallet {
  @PrimaryGeneratedColumn()
  id: number;

  @Column()
  walletId: string;

  @Column()
  walletAddress: string;

  @Column()
  walletBalance: number;

  @Column()
  walletStatus: string;
}
