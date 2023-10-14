import { Client } from 'pg';

export function createDatabaseClient(): Client {
  const client = new Client({
    user: 'seu_usuario',
    host: 'seu_host',
    database: 'seu_banco_de_dados',
    password: 'sua_senha',
    port: '',
  });

  return client;
}
