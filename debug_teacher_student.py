from src.open_r1.run_teacher_student import main, TrlParser, GRPOScriptArguments, TeacherStudentGRPOConfig, TeacherStudentConfig

if __name__ == '__main__':
    parser = TrlParser((GRPOScriptArguments, TeacherStudentGRPOConfig, TeacherStudentConfig))
    script_args, training_args, model_args = parser.parse_args_and_config()
    main(script_args, training_args, model_args)