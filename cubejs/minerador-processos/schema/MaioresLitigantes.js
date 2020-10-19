cube(`MaioresLitigantes`, {
  sql: `SELECT * FROM minerador_processos.mv_maiores_litigantes`,
  
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
    
    nmOrgao: {
      sql: `nm_orgao`,
      type: `string`
    },
    
    dsGrauOrgao: {
      sql: `ds_grau`,
      type: `string`
    },
    
    sgTribunal: {
      sql: `sg_tribunal`,
      type: `string`
    },
    
    nmPessoa: {
      sql: `nm_pessoa`,
      type: `string`
    },
    
    nrDocPrincipalPessoa: {
      sql: `nr_doc_principal_pessoa`,
      type: `string`
    },
    
    nmOrgaoMovimento: {
      sql: `nm_orgao_movimento`,
      type: `string`
    },
    
    dtAjuizamento: {
      sql: `dt_ajuizamento`,
      type: `time`
    },
    
    dtLancamentoMovimento: {
      sql: `dt_lancamento_movimento`,
      type: `time`
    },

    dsMovimento: {
      sql: `ds_movimento`,
      type: `string`
    },


    nrClasseProcessual: {
      sql: `nr_classe_processual`,
      type: `number`
    },

    cdMunicipioOrgaoMovimento: {
      sql: `cd_municipio_orgao_movimento`,
      type: `number`
    },

    dsMovimentoComplementos: {
      sql: `ds_movimento_complementos`,
      type: `string`
    }

  }
});
