def set_project_year(project_year: int):
    if (len(str(project_year))) == 4:
        project_year -= 1911
        return project_year

    return project_year
