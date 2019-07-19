import { AppConfig } from '../../core/app-config';
import { Topic } from '../../shared/models/topics/topic';
import { TopicRepositoryService } from 'app/core/repositories/topics/topic-repository.service';
import { ViewTopic } from './models/view-topic';

export const TopicsAppConfig: AppConfig = {
    name: 'topics',
    models: [
        {
            collectionString: 'topics/topic',
            model: Topic,
            viewModel: ViewTopic,
            searchOrder: 1,
            repository: TopicRepositoryService
        }
    ]
};