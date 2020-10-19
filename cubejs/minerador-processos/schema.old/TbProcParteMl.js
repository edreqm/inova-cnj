cube(`TbProcParteMl`, {
  sql: `SELECT * FROM minerador_processos.tb_proc_parte_ml`,
  
  joins: {
    
  },
  
  measures: {
    count: {
      type: `count`,
      drillMembers: []
    }
  },
  
  dimensions: {
    nrProcesso: {
      sql: `nr_processo`,
      type: `string`
    },
    
    nrChaveProc: {
      sql: `nr_chave_proc`,
      type: `string`
    },
    
    nmPessoa: {
      sql: `nm_pessoa`,
      type: `string`
    },
    
    nrDocPrincipalPessoa: {
      sql: `nr_doc_principal_pessoa`,
      type: `string`
    }
  }
});
