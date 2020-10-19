cube(`TbProcesso`, {
  sql: `SELECT * FROM minerador_processos.tb_processo`,
  
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
      sql: `ds_grau_orgao`,
      type: `string`
    },
    
    sgTribunal: {
      sql: `sg_tribunal`,
      type: `string`
    },
    
    tpPolo: {
      sql: `tp_polo`,
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
    
    nmAdvogado: {
      sql: `nm_advogado`,
      type: `string`
    },
    
    nrInscricaoAdvogado: {
      sql: `nr_inscricao_advogado`,
      type: `string`
    },
    
    tpRepresentante: {
      sql: `tp_representante`,
      type: `string`
    },
    
    cdAssuntoPrincipal: {
      sql: `cd_assunto_principal`,
      type: `string`
    },
    
    nmOrgaoMovimento: {
      sql: `nm_orgao_movimento`,
      type: `string`
    },
    
    dsComplementoMovimentoNacional: {
      sql: `ds_complemento_movimento_nacional`,
      type: `string`
    },
    
    dtAjuizamento: {
      sql: `dt_ajuizamento`,
      type: `time`
    },
    
    dtLancamentoMovimento: {
      sql: `dt_lancamento_movimento`,
      type: `time`
    }
  }
});
