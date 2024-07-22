{
    "targets": [
        {
            "target_name": "<(module_name)", 
            "variables": {
                "include_httpfs": "<!(echo ${DUCKDB_INCLUDE_HTTPFS})"
            }, 
            "sources": [
                "src/duckdb_node.cpp", 
                "src/database.cpp", 
                "src/data_chunk.cpp", 
                "src/connection.cpp", 
                "src/statement.cpp", 
                "src/utils.cpp", 
                "src/duckdb/ub_src_catalog.cpp", 
                "src/duckdb/ub_src_catalog_catalog_entry.cpp", 
                "src/duckdb/ub_src_catalog_catalog_entry_dependency.cpp", 
                "src/duckdb/ub_src_catalog_default.cpp", 
                "src/duckdb/ub_src_common_adbc.cpp", 
                "src/duckdb/ub_src_common_adbc_nanoarrow.cpp", 
                "src/duckdb/ub_src_common.cpp", 
                "src/duckdb/ub_src_common_arrow_appender.cpp", 
                "src/duckdb/ub_src_common_arrow.cpp", 
                "src/duckdb/ub_src_common_crypto.cpp", 
                "src/duckdb/ub_src_common_enums.cpp", 
                "src/duckdb/ub_src_common_exception.cpp", 
                "src/duckdb/ub_src_common_operator.cpp", 
                "src/duckdb/ub_src_common_progress_bar.cpp", 
                "src/duckdb/ub_src_common_row_operations.cpp", 
                "src/duckdb/ub_src_common_serializer.cpp", 
                "src/duckdb/ub_src_common_sort.cpp", 
                "src/duckdb/ub_src_common_types.cpp", 
                "src/duckdb/ub_src_common_types_column.cpp", 
                "src/duckdb/ub_src_common_types_row.cpp", 
                "src/duckdb/ub_src_common_value_operations.cpp", 
                "src/duckdb/src/common/vector_operations/boolean_operators.cpp", 
                "src/duckdb/src/common/vector_operations/comparison_operators.cpp", 
                "src/duckdb/src/common/vector_operations/generators.cpp", 
                "src/duckdb/src/common/vector_operations/is_distinct_from.cpp", 
                "src/duckdb/src/common/vector_operations/null_operations.cpp", 
                "src/duckdb/src/common/vector_operations/numeric_inplace_operators.cpp", 
                "src/duckdb/src/common/vector_operations/vector_cast.cpp", 
                "src/duckdb/src/common/vector_operations/vector_copy.cpp", 
                "src/duckdb/src/common/vector_operations/vector_hash.cpp", 
                "src/duckdb/src/common/vector_operations/vector_storage.cpp", 
                "src/duckdb/ub_src_core_functions_aggregate_algebraic.cpp", 
                "src/duckdb/ub_src_core_functions_aggregate_distributive.cpp", 
                "src/duckdb/ub_src_core_functions_aggregate_holistic.cpp", 
                "src/duckdb/ub_src_core_functions_aggregate_nested.cpp", 
                "src/duckdb/ub_src_core_functions_aggregate_regression.cpp", 
                "src/duckdb/ub_src_core_functions.cpp", 
                "src/duckdb/ub_src_core_functions_scalar_array.cpp", 
                "src/duckdb/ub_src_core_functions_scalar_bit.cpp", 
                "src/duckdb/ub_src_core_functions_scalar_blob.cpp", 
                "src/duckdb/ub_src_core_functions_scalar_date.cpp", 
                "src/duckdb/ub_src_core_functions_scalar_debug.cpp", 
                "src/duckdb/ub_src_core_functions_scalar_enum.cpp", 
                "src/duckdb/ub_src_core_functions_scalar_generic.cpp", 
                "src/duckdb/ub_src_core_functions_scalar_list.cpp", 
                "src/duckdb/ub_src_core_functions_scalar_map.cpp", 
                "src/duckdb/ub_src_core_functions_scalar_math.cpp", 
                "src/duckdb/ub_src_core_functions_scalar_operators.cpp", 
                "src/duckdb/ub_src_core_functions_scalar_random.cpp", 
                "src/duckdb/ub_src_core_functions_scalar_string.cpp", 
                "src/duckdb/ub_src_core_functions_scalar_struct.cpp", 
                "src/duckdb/ub_src_core_functions_scalar_union.cpp", 
                "src/duckdb/ub_src_execution.cpp", 
                "src/duckdb/ub_src_execution_expression_executor.cpp", 
                "src/duckdb/ub_src_execution_index_art.cpp", 
                "src/duckdb/ub_src_execution_index.cpp", 
                "src/duckdb/ub_src_execution_nested_loop_join.cpp", 
                "src/duckdb/ub_src_execution_operator_aggregate.cpp", 
                "src/duckdb/ub_src_execution_operator_csv_scanner_buffer_manager.cpp", 
                "src/duckdb/ub_src_execution_operator_csv_scanner_scanner.cpp", 
                "src/duckdb/ub_src_execution_operator_csv_scanner_sniffer.cpp", 
                "src/duckdb/ub_src_execution_operator_csv_scanner_state_machine.cpp", 
                "src/duckdb/ub_src_execution_operator_csv_scanner_table_function.cpp", 
                "src/duckdb/ub_src_execution_operator_csv_scanner_util.cpp", 
                "src/duckdb/ub_src_execution_operator_filter.cpp", 
                "src/duckdb/ub_src_execution_operator_helper.cpp", 
                "src/duckdb/ub_src_execution_operator_join.cpp", 
                "src/duckdb/ub_src_execution_operator_order.cpp", 
                "src/duckdb/ub_src_execution_operator_persistent.cpp", 
                "src/duckdb/ub_src_execution_operator_projection.cpp", 
                "src/duckdb/ub_src_execution_operator_scan.cpp", 
                "src/duckdb/ub_src_execution_operator_schema.cpp", 
                "src/duckdb/ub_src_execution_operator_set.cpp", 
                "src/duckdb/ub_src_execution_physical_plan.cpp", 
                "src/duckdb/ub_src_function_aggregate_distributive.cpp", 
                "src/duckdb/ub_src_function_aggregate.cpp", 
                "src/duckdb/ub_src_function.cpp", 
                "src/duckdb/ub_src_function_cast.cpp", 
                "src/duckdb/ub_src_function_cast_union.cpp", 
                "src/duckdb/ub_src_function_pragma.cpp", 
                "src/duckdb/ub_src_function_scalar_compressed_materialization.cpp", 
                "src/duckdb/ub_src_function_scalar.cpp", 
                "src/duckdb/ub_src_function_scalar_generic.cpp", 
                "src/duckdb/ub_src_function_scalar_list.cpp", 
                "src/duckdb/ub_src_function_scalar_operators.cpp", 
                "src/duckdb/ub_src_function_scalar_sequence.cpp", 
                "src/duckdb/ub_src_function_scalar_string.cpp", 
                "src/duckdb/ub_src_function_scalar_string_regexp.cpp", 
                "src/duckdb/ub_src_function_scalar_struct.cpp", 
                "src/duckdb/ub_src_function_scalar_system.cpp", 
                "src/duckdb/ub_src_function_table_arrow.cpp", 
                "src/duckdb/ub_src_function_table.cpp", 
                "src/duckdb/ub_src_function_table_system.cpp", 
                "src/duckdb/ub_src_function_table_version.cpp", 
                "src/duckdb/ub_src_main.cpp", 
                "src/duckdb/ub_src_main_buffered_data.cpp", 
                "src/duckdb/ub_src_main_capi.cpp", 
                "src/duckdb/ub_src_main_capi_cast.cpp", 
                "src/duckdb/ub_src_main_chunk_scan_state.cpp", 
                "src/duckdb/ub_src_main_extension.cpp", 
                "src/duckdb/ub_src_main_relation.cpp", 
                "src/duckdb/ub_src_main_secret.cpp", 
                "src/duckdb/ub_src_main_settings.cpp", 
                "src/duckdb/ub_src_optimizer.cpp", 
                "src/duckdb/ub_src_optimizer_compressed_materialization.cpp", 
                "src/duckdb/ub_src_optimizer_join_order.cpp", 
                "src/duckdb/ub_src_optimizer_matcher.cpp", 
                "src/duckdb/ub_src_optimizer_pullup.cpp", 
                "src/duckdb/ub_src_optimizer_pushdown.cpp", 
                "src/duckdb/ub_src_optimizer_rule.cpp", 
                "src/duckdb/ub_src_optimizer_statistics_expression.cpp", 
                "src/duckdb/ub_src_optimizer_statistics_operator.cpp", 
                "src/duckdb/ub_src_parallel.cpp", 
                "src/duckdb/ub_src_parser.cpp", 
                "src/duckdb/ub_src_parser_constraints.cpp", 
                "src/duckdb/ub_src_parser_expression.cpp", 
                "src/duckdb/ub_src_parser_parsed_data.cpp", 
                "src/duckdb/ub_src_parser_query_node.cpp", 
                "src/duckdb/ub_src_parser_statement.cpp", 
                "src/duckdb/ub_src_parser_tableref.cpp", 
                "src/duckdb/ub_src_parser_transform_constraint.cpp", 
                "src/duckdb/ub_src_parser_transform_expression.cpp", 
                "src/duckdb/ub_src_parser_transform_helpers.cpp", 
                "src/duckdb/ub_src_parser_transform_statement.cpp", 
                "src/duckdb/ub_src_parser_transform_tableref.cpp", 
                "src/duckdb/ub_src_planner.cpp", 
                "src/duckdb/ub_src_planner_binder_expression.cpp", 
                "src/duckdb/ub_src_planner_binder_query_node.cpp", 
                "src/duckdb/ub_src_planner_binder_statement.cpp", 
                "src/duckdb/ub_src_planner_binder_tableref.cpp", 
                "src/duckdb/ub_src_planner_expression.cpp", 
                "src/duckdb/ub_src_planner_expression_binder.cpp", 
                "src/duckdb/ub_src_planner_filter.cpp", 
                "src/duckdb/ub_src_planner_operator.cpp", 
                "src/duckdb/ub_src_planner_subquery.cpp", 
                "src/duckdb/ub_src_storage.cpp", 
                "src/duckdb/ub_src_storage_buffer.cpp", 
                "src/duckdb/ub_src_storage_checkpoint.cpp", 
                "src/duckdb/ub_src_storage_compression_alp.cpp", 
                "src/duckdb/ub_src_storage_compression.cpp", 
                "src/duckdb/ub_src_storage_compression_chimp.cpp", 
                "src/duckdb/ub_src_storage_metadata.cpp", 
                "src/duckdb/ub_src_storage_serialization.cpp", 
                "src/duckdb/ub_src_storage_statistics.cpp", 
                "src/duckdb/ub_src_storage_table.cpp", 
                "src/duckdb/ub_src_transaction.cpp", 
                "src/duckdb/src/verification/copied_statement_verifier.cpp", 
                "src/duckdb/src/verification/deserialized_statement_verifier.cpp", 
                "src/duckdb/src/verification/external_statement_verifier.cpp", 
                "src/duckdb/src/verification/fetch_row_verifier.cpp", 
                "src/duckdb/src/verification/no_operator_caching_verifier.cpp", 
                "src/duckdb/src/verification/parsed_statement_verifier.cpp", 
                "src/duckdb/src/verification/prepared_statement_verifier.cpp", 
                "src/duckdb/src/verification/statement_verifier.cpp", 
                "src/duckdb/src/verification/unoptimized_statement_verifier.cpp", 
                "src/duckdb/third_party/fmt/format.cc", 
                "src/duckdb/third_party/fsst/libfsst.cpp", 
                "src/duckdb/third_party/miniz/miniz.cpp", 
                "src/duckdb/third_party/re2/re2/bitmap256.cc", 
                "src/duckdb/third_party/re2/re2/bitstate.cc", 
                "src/duckdb/third_party/re2/re2/compile.cc", 
                "src/duckdb/third_party/re2/re2/dfa.cc", 
                "src/duckdb/third_party/re2/re2/filtered_re2.cc", 
                "src/duckdb/third_party/re2/re2/mimics_pcre.cc", 
                "src/duckdb/third_party/re2/re2/nfa.cc", 
                "src/duckdb/third_party/re2/re2/onepass.cc", 
                "src/duckdb/third_party/re2/re2/parse.cc", 
                "src/duckdb/third_party/re2/re2/perl_groups.cc", 
                "src/duckdb/third_party/re2/re2/prefilter.cc", 
                "src/duckdb/third_party/re2/re2/prefilter_tree.cc", 
                "src/duckdb/third_party/re2/re2/prog.cc", 
                "src/duckdb/third_party/re2/re2/re2.cc", 
                "src/duckdb/third_party/re2/re2/regexp.cc", 
                "src/duckdb/third_party/re2/re2/set.cc", 
                "src/duckdb/third_party/re2/re2/simplify.cc", 
                "src/duckdb/third_party/re2/re2/stringpiece.cc", 
                "src/duckdb/third_party/re2/re2/tostring.cc", 
                "src/duckdb/third_party/re2/re2/unicode_casefold.cc", 
                "src/duckdb/third_party/re2/re2/unicode_groups.cc", 
                "src/duckdb/third_party/re2/util/rune.cc", 
                "src/duckdb/third_party/re2/util/strutil.cc", 
                "src/duckdb/third_party/hyperloglog/hyperloglog.cpp", 
                "src/duckdb/third_party/hyperloglog/sds.cpp", 
                "src/duckdb/third_party/skiplist/SkipList.cpp", 
                "src/duckdb/third_party/fastpforlib/bitpacking.cpp", 
                "src/duckdb/third_party/utf8proc/utf8proc.cpp", 
                "src/duckdb/third_party/utf8proc/utf8proc_wrapper.cpp", 
                "src/duckdb/third_party/libpg_query/pg_functions.cpp", 
                "src/duckdb/third_party/libpg_query/postgres_parser.cpp", 
                "src/duckdb/third_party/libpg_query/src_backend_nodes_list.cpp", 
                "src/duckdb/third_party/libpg_query/src_backend_nodes_makefuncs.cpp", 
                "src/duckdb/third_party/libpg_query/src_backend_nodes_value.cpp", 
                "src/duckdb/third_party/libpg_query/src_backend_parser_gram.cpp", 
                "src/duckdb/third_party/libpg_query/src_backend_parser_parser.cpp", 
                "src/duckdb/third_party/libpg_query/src_backend_parser_scan.cpp", 
                "src/duckdb/third_party/libpg_query/src_backend_parser_scansup.cpp", 
                "src/duckdb/third_party/libpg_query/src_common_keywords.cpp", 
                "src/duckdb/third_party/mbedtls/library/aes.cpp", 
                "src/duckdb/third_party/mbedtls/library/aria.cpp", 
                "src/duckdb/third_party/mbedtls/library/asn1parse.cpp", 
                "src/duckdb/third_party/mbedtls/library/base64.cpp", 
                "src/duckdb/third_party/mbedtls/library/bignum.cpp", 
                "src/duckdb/third_party/mbedtls/library/camellia.cpp", 
                "src/duckdb/third_party/mbedtls/library/cipher.cpp", 
                "src/duckdb/third_party/mbedtls/library/cipher_wrap.cpp", 
                "src/duckdb/third_party/mbedtls/library/constant_time.cpp", 
                "src/duckdb/third_party/mbedtls/library/entropy.cpp", 
                "src/duckdb/third_party/mbedtls/library/entropy_poll.cpp", 
                "src/duckdb/third_party/mbedtls/library/gcm.cpp", 
                "src/duckdb/third_party/mbedtls/library/md.cpp", 
                "src/duckdb/third_party/mbedtls/library/oid.cpp", 
                "src/duckdb/third_party/mbedtls/library/pem.cpp", 
                "src/duckdb/third_party/mbedtls/library/pk.cpp", 
                "src/duckdb/third_party/mbedtls/library/pk_wrap.cpp", 
                "src/duckdb/third_party/mbedtls/library/pkparse.cpp", 
                "src/duckdb/third_party/mbedtls/library/platform_util.cpp", 
                "src/duckdb/third_party/mbedtls/library/rsa.cpp", 
                "src/duckdb/third_party/mbedtls/library/rsa_alt_helpers.cpp", 
                "src/duckdb/third_party/mbedtls/library/sha1.cpp", 
                "src/duckdb/third_party/mbedtls/library/sha256.cpp", 
                "src/duckdb/third_party/mbedtls/library/sha512.cpp", 
                "src/duckdb/third_party/mbedtls/mbedtls_wrapper.cpp", 
                "src/duckdb/third_party/yyjson/yyjson.cpp", 
                "src/duckdb/extension/parquet/column_reader.cpp", 
                "src/duckdb/extension/parquet/column_writer.cpp", 
                "src/duckdb/extension/parquet/parquet_crypto.cpp", 
                "src/duckdb/extension/parquet/parquet_extension.cpp", 
                "src/duckdb/extension/parquet/parquet_metadata.cpp", 
                "src/duckdb/extension/parquet/parquet_reader.cpp", 
                "src/duckdb/extension/parquet/parquet_statistics.cpp", 
                "src/duckdb/extension/parquet/parquet_timestamp.cpp", 
                "src/duckdb/extension/parquet/parquet_writer.cpp", 
                "src/duckdb/extension/parquet/serialize_parquet.cpp", 
                "src/duckdb/extension/parquet/zstd_file_system.cpp", 
                "src/duckdb/third_party/parquet/parquet_constants.cpp", 
                "src/duckdb/third_party/parquet/parquet_types.cpp", 
                "src/duckdb/third_party/thrift/thrift/protocol/TProtocol.cpp", 
                "src/duckdb/third_party/thrift/thrift/transport/TTransportException.cpp", 
                "src/duckdb/third_party/thrift/thrift/transport/TBufferTransports.cpp", 
                "src/duckdb/third_party/snappy/snappy.cc", 
                "src/duckdb/third_party/snappy/snappy-sinksource.cc", 
                "src/duckdb/third_party/zstd/decompress/zstd_ddict.cpp", 
                "src/duckdb/third_party/zstd/decompress/huf_decompress.cpp", 
                "src/duckdb/third_party/zstd/decompress/zstd_decompress.cpp", 
                "src/duckdb/third_party/zstd/decompress/zstd_decompress_block.cpp", 
                "src/duckdb/third_party/zstd/common/entropy_common.cpp", 
                "src/duckdb/third_party/zstd/common/fse_decompress.cpp", 
                "src/duckdb/third_party/zstd/common/zstd_common.cpp", 
                "src/duckdb/third_party/zstd/common/error_private.cpp", 
                "src/duckdb/third_party/zstd/common/xxhash.cpp", 
                "src/duckdb/third_party/zstd/compress/fse_compress.cpp", 
                "src/duckdb/third_party/zstd/compress/hist.cpp", 
                "src/duckdb/third_party/zstd/compress/huf_compress.cpp", 
                "src/duckdb/third_party/zstd/compress/zstd_compress.cpp", 
                "src/duckdb/third_party/zstd/compress/zstd_compress_literals.cpp", 
                "src/duckdb/third_party/zstd/compress/zstd_compress_sequences.cpp", 
                "src/duckdb/third_party/zstd/compress/zstd_compress_superblock.cpp", 
                "src/duckdb/third_party/zstd/compress/zstd_double_fast.cpp", 
                "src/duckdb/third_party/zstd/compress/zstd_fast.cpp", 
                "src/duckdb/third_party/zstd/compress/zstd_lazy.cpp", 
                "src/duckdb/third_party/zstd/compress/zstd_ldm.cpp", 
                "src/duckdb/third_party/zstd/compress/zstd_opt.cpp", 
                "src/duckdb/third_party/lz4/lz4.cpp", 
                "src/duckdb/extension/icu/./icu-table-range.cpp", 
                "src/duckdb/extension/icu/./icu-makedate.cpp", 
                "src/duckdb/extension/icu/./icu-list-range.cpp", 
                "src/duckdb/extension/icu/./icu-timebucket.cpp", 
                "src/duckdb/extension/icu/./icu-timezone.cpp", 
                "src/duckdb/extension/icu/./icu-dateadd.cpp", 
                "src/duckdb/extension/icu/./icu-datetrunc.cpp", 
                "src/duckdb/extension/icu/./icu-datesub.cpp", 
                "src/duckdb/extension/icu/./icu_extension.cpp", 
                "src/duckdb/extension/icu/./icu-strptime.cpp", 
                "src/duckdb/extension/icu/./icu-datefunc.cpp", 
                "src/duckdb/extension/icu/./icu-datepart.cpp", 
                "src/duckdb/ub_extension_icu_third_party_icu_common.cpp", 
                "src/duckdb/ub_extension_icu_third_party_icu_i18n.cpp", 
                "src/duckdb/extension/icu/third_party/icu/stubdata/stubdata.cpp", 
                "src/duckdb/extension/json/buffered_json_reader.cpp", 
                "src/duckdb/extension/json/json_enums.cpp", 
                "src/duckdb/extension/json/json_extension.cpp", 
                "src/duckdb/extension/json/json_common.cpp", 
                "src/duckdb/extension/json/json_functions.cpp", 
                "src/duckdb/extension/json/json_scan.cpp", 
                "src/duckdb/extension/json/json_serializer.cpp", 
                "src/duckdb/extension/json/json_deserializer.cpp", 
                "src/duckdb/extension/json/serialize_json.cpp", 
                "src/duckdb/ub_extension_json_json_functions.cpp"
            ], 
            "include_dirs": [
                "<!(node -p \"require('node-addon-api').include_dir\")", 
                "src/duckdb/src/include", 
                "src/duckdb/third_party/concurrentqueue", 
                "src/duckdb/third_party/fast_float", 
                "src/duckdb/third_party/fastpforlib", 
                "src/duckdb/third_party/fmt/include", 
                "src/duckdb/third_party/fsst", 
                "src/duckdb/third_party/httplib", 
                "src/duckdb/third_party/hyperloglog", 
                "src/duckdb/third_party/jaro_winkler", 
                "src/duckdb/third_party/jaro_winkler/details", 
                "src/duckdb/third_party/libpg_query", 
                "src/duckdb/third_party/libpg_query/include", 
                "src/duckdb/third_party/lz4", 
                "src/duckdb/third_party/mbedtls", 
                "src/duckdb/third_party/mbedtls/include", 
                "src/duckdb/third_party/mbedtls/library", 
                "src/duckdb/third_party/miniz", 
                "src/duckdb/third_party/pcg", 
                "src/duckdb/third_party/re2", 
                "src/duckdb/third_party/skiplist", 
                "src/duckdb/third_party/tdigest", 
                "src/duckdb/third_party/utf8proc", 
                "src/duckdb/third_party/utf8proc/include", 
                "src/duckdb/third_party/yyjson/include", 
                "src/duckdb/extension/parquet/include", 
                "src/duckdb/third_party/parquet", 
                "src/duckdb/third_party/thrift", 
                "src/duckdb/third_party/lz4", 
                "src/duckdb/third_party/snappy", 
                "src/duckdb/third_party/zstd/include", 
                "src/duckdb/third_party/mbedtls", 
                "src/duckdb/third_party/mbedtls/include", 
                "src/duckdb/extension/icu/include", 
                "src/duckdb/extension/icu/third_party/icu/common", 
                "src/duckdb/extension/icu/third_party/icu/i18n", 
                "src/duckdb/extension/json/include"
            ], 
            "defines": [
                "NAPI_VERSION=6", 
                "DUCKDB_EXTENSION_PARQUET_LINKED", 
                "DUCKDB_EXTENSION_ICU_LINKED", 
                "DUCKDB_EXTENSION_JSON_LINKED", 
                "DUCKDB_EXTENSION_AUTOLOAD_DEFAULT=1", 
                "DUCKDB_EXTENSION_AUTOINSTALL_DEFAULT=1"
            ], 
            "cflags_cc": [
                "-frtti", 
                "-fexceptions", 
                "-Wno-redundant-move"
            ], 
            "cflags_cc!": [
                "-fno-rrti", 
                "-fno-exceptions"
            ], 
            "cflags": [
                "-frtti", 
                "-fexceptions", 
                "-Wno-redundant-move", 
                "-frtti"
            ], 
            "cflags!": [
                "-fno-rrti", 
                "-fno-exceptions"
            ], 
            "xcode_settings": {
                "GCC_ENABLE_CPP_EXCEPTIONS": "YES", 
                "GCC_ENABLE_CPP_RTTI": "YES", 
                "CLANG_CXX_LIBRARY": "libc++", 
                "MACOSX_DEPLOYMENT_TARGET": "10.15", 
                "CLANG_CXX_LANGUAGE_STANDARD": "c++11", 
                "OTHER_CFLAGS": [
                    "-fexceptions", 
                    "-frtti", 
                    "-Wno-redundant-move"
                ]
            }, 
            "msvs_settings": {
                "VCCLCompilerTool": {
                    "ExceptionHandling": 1, 
                    "AdditionalOptions": [
                        "/bigobj", 
                        "/GR"
                    ]
                }
            }, 
            "conditions": [
                [
                    "OS==\"win\"", 
                    {
                        "defines": [
                            "DUCKDB_BUILD_LIBRARY"
                        ], 
                        "libraries": [
                            "rstrtmgr.lib", 
                            "bcrypt.lib"
                        ]
                    }
                ], 
                [
                    "include_httpfs=='true'", 
                    {
                        "sources": [
                            "src/duckdb/extension/httpfs/create_secret_functions.cpp", 
                            "src/duckdb/extension/httpfs/crypto.cpp", 
                            "src/duckdb/extension/httpfs/hffs.cpp", 
                            "src/duckdb/extension/httpfs/httpfs.cpp", 
                            "src/duckdb/extension/httpfs/httpfs_extension.cpp", 
                            "src/duckdb/extension/httpfs/s3fs.cpp"
                        ], 
                        "include_dirs": [
                            "src/duckdb/extension/httpfs/include"
                        ], 
                        "defines": [
                            "DUCKDB_EXTENSION_HTTPFS_LINKED"
                        ]
                    }
                ]
            ], 
            "libraries": []
        }, 
        {
            "target_name": "action_after_build", 
            "type": "none", 
            "dependencies": [
                "<(module_name)"
            ], 
            "copies": [
                {
                    "files": [
                        "<(PRODUCT_DIR)/<(module_name).node"
                    ], 
                    "destination": "<(module_path)"
                }
            ]
        }
    ]
}