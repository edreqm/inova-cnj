cube(`PerformanceVara`, {
  sql: `SELECT * FROM minerador_processos.tb_fitness_vara`,
  
  joins: {
    
  },
  
  measures: {
    fitness: {
      sql: `vl_fitness`,
      type: `avg`,
      drillMembers: []
    },

    tempo: {
      sql: `nr_dias`,
      type: `avg`,
      drillMembers: []
    }
  },
  
  dimensions: {
    nomeDaVara: {
      sql: `cd_orgao`,
      type: `string`
    },
    
    nomeDoLitigante: {
      sql: `nr_doc_principal_pessoa`,
      type: `string`
    }
  }
});
